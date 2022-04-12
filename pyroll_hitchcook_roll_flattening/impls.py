import numpy as np
import logging
from pyroll import RollPass

log = logging.getLogger(__name__)


@RollPass.hookimpl
def roll_poissons_ratio(roll_pass):
    return 0.3


@RollPass.hookimpl
def roll_youngs_modulus(roll_pass):
    return 210e6


@RollPass.hookimpl
def flattened_radius_nominal_radius_ratio(roll_pass):
    flattening_hitchcock = 16 / np.pi * (1 - roll_pass.roll_poissons_ratio ** 2) \
                           / roll_pass.roll_youngs_modulus * roll_pass.roll_force / \
                           (roll_pass.in_profile.equivalent_rectangle.height - roll_pass.gap)

    log.debug(f"Calculated radius ratio of {flattening_hitchcock:.2f}")

    if flattening_hitchcock < 4.235:
        return 1 + flattening_hitchcock
    else:
        return 2 * flattening_hitchcock ** (2 / 3)


@RollPass.hookimpl
def flattened_roll_radius(roll_pass):
    if "roll_force" not in roll_pass.__dict__:
        return roll_pass.nominal_roll_radius
    else:
        flattened_radius = roll_pass.flattened_radius_nominal_radius_ratio * roll_pass.nominal_roll_radius
        log.info(f"Calculated a roll radius of {flattened_radius:.2f} mm using Hitchcook's model!")
        return flattened_radius


@RollPass.hookimpl
def max_roll_radius(roll_pass):
    max_radius = roll_pass.flattened_roll_radius
    log.debug(f"Calculated a maximal roll radius of {max_radius:.2f} mm")
    return max_radius


@RollPass.hookimpl
def min_roll_radius(roll_pass):
    min_radius = roll_pass.flattened_roll_radius - roll_pass.groove.depth
    log.info(f"Calculated a minimal roll radius of {min_radius:.2f} mm")
    return min_radius


@RollPass.hookimpl
def working_roll_radius(roll_pass):
    return roll_pass.flattened_roll_radius - roll_pass.groove.cross_section.centroid.y

