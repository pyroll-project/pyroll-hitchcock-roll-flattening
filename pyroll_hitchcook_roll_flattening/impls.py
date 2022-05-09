import numpy as np
import logging
from pyroll import RollPass, Roll

log = logging.getLogger(__name__)


@Roll.hookimpl
def poissons_ratio():
    return 0.3


@Roll.hookimpl
def elastic_modulus():
    return 210e6


@RollPass.Roll.hookimpl
def flattening_ratio(roll: RollPass.Roll, roll_pass: RollPass):
    flattening_hitchcock = 16 / np.pi * (1 - roll_pass.roll.poissons_ratio ** 2) \
                           / roll_pass.roll.elastic_modulus * roll_pass.roll_force / \
                           (roll_pass.in_profile.equivalent_rectangle.height - roll_pass.gap)

    log.debug(f"Calculated radius ratio of {flattening_hitchcock:.2f}")

    if flattening_hitchcock < 4.235:
        return 1 + flattening_hitchcock
    else:
        return 2 * flattening_hitchcock ** (2 / 3)


@RollPass.Roll.hookimpl
def flattened_radius(roll: RollPass.Roll, roll_pass: RollPass):
    if "roll_force" not in roll_pass.__dict__:
        return roll_pass.nominal_roll_radius
    else:
        flattened_radius = roll.flattening_ratio * roll.nominal_radius
        log.info(f"Calculated a roll radius of {flattened_radius * 1e3:.2f} mm using Hitchcook's model!")
        return flattened_radius


@Roll.hookimpl
def max_roll_radius(roll: Roll):
    if not hasattr(roll, "flattened_radius"):
        return None

    r = roll.flattened_radius
    return r


@Roll.hookimpl
def min_roll_radius(roll: Roll):
    if not hasattr(roll, "flattened_radius"):
        return None

    r = roll.flattened_radius - roll.groove.depth
    return r


@Roll.hookimpl
def working_roll_radius(roll: Roll):
    if not hasattr(roll, "flattened_radius"):
        return None

    r = roll.flattened_radius - roll.groove.cross_section.centroid.y
    return r
