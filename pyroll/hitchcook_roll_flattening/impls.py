import numpy as np
import logging
from pyroll.core import RollPass, Roll

log = logging.getLogger(__name__)


@Roll.hookimpl
def poissons_ratio(roll: Roll):
    """Default implementation for steel rolls."""
    return 0.3


@Roll.hookimpl
def youngs_modulus(roll: Roll):
    """Default implementation for steel rolls."""
    return 210e9


@RollPass.Roll.hookimpl
def flattening_ratio(roll: Roll, roll_pass: RollPass):
    """Calculates the ratio between flattened and initial roll radius using Hitchcooks formula."""

    elastic_constant = (16 * (1 - roll.poissons_ratio ** 2)) / (np.pi * roll.youngs_modulus)
    height_change = roll_pass.in_profile.equivalent_rectangle.height - roll_pass.out_profile.equivalent_rectangle.height
    mean_width = (roll_pass.in_profile.equivalent_rectangle.width + roll_pass.out_profile.equivalent_rectangle.width) / 2

    flattening_hitchcock = (elastic_constant * roll_pass.roll_force) / (height_change * mean_width)

    if flattening_hitchcock < 4.235:
        ratio = 1 + flattening_hitchcock

    else:
        ratio = 2 * flattening_hitchcock ** (2 / 3)

    log.info(f"Calculated radius ratio of {ratio:.2f}")
    return ratio


@RollPass.Roll.hookimpl
def flattened_radius(roll: Roll, roll_pass: RollPass):
    """Calculates the flattened radius."""
    if "roll_force" not in roll_pass.__dict__:
        radius = roll.nominal_radius
    else:

        radius = roll_pass.roll.flattening_ratio * roll_pass.roll.nominal_radius
        log.info(f"Calculated a roll radius of {radius * 1e3:.2f} mm using Hitchcook's model!")

    return radius


@Roll.hookimpl
def max_radius(roll: Roll):
    if not hasattr(roll, "flattened_radius"):
        return None

    radius = roll.flattened_radius
    return radius


@Roll.hookimpl
def min_radius(roll: Roll):
    if not hasattr(roll, "flattened_radius"):
        return None

    radius = roll.flattened_radius - roll.groove.depth
    return radius


@Roll.hookimpl
def working_radius(roll: Roll):
    if not hasattr(roll, "flattened_radius"):
        return None

    radius = roll.flattened_radius - roll.groove.cross_section.centroid.y
    return radius
