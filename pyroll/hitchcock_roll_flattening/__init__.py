from pyroll.core import RollPass, Roll

import numpy as np
import logging
from pyroll.core import RollPass, Roll, Hook

log = logging.getLogger(__name__)

RollPass.Roll.flattening_ratio = Hook[float]()
"""The ratio between flattened and nominal radius of the roll."""

RollPass.Roll.flattened_radius = Hook[float]()
"""Flattened roll radius acc. to Hitchcock."""


@Roll.poissons_ratio
def default_poissons_ratio(roll: Roll):
    """Default implementation for steel rolls."""
    return 0.3


@Roll.elastic_modulus
def default_elastic_modulus(roll: Roll):
    """Default implementation for steel rolls."""
    return 210e9


@RollPass.Roll.flattening_ratio
def flattening_ratio(self: RollPass.Roll):
    """Calculates the ratio between flattened and initial roll radius using Hitchcooks formula."""
    roll_pass = self.roll_pass()

    elastic_constant = (16 * (1 - self.poissons_ratio ** 2)) / (np.pi * self.elastic_modulus)
    height_change = roll_pass.in_profile.equivalent_rectangle.height - roll_pass.out_profile.equivalent_rectangle.height
    mean_width = (
                         roll_pass.in_profile.equivalent_rectangle.width + roll_pass.out_profile.equivalent_rectangle.width) / 2

    flattening_hitchcock = (elastic_constant * roll_pass.roll_force) / (height_change * mean_width)

    if flattening_hitchcock < 4.235:
        ratio = 1 + flattening_hitchcock

    else:
        ratio = 2 * flattening_hitchcock ** (2 / 3)

    log.info(f"Calculated radius ratio of {ratio:.2f}")
    return ratio


@RollPass.Roll.flattened_radius
def flattened_radius(self: RollPass.Roll):
    """Calculates the flattened radius."""
    roll_pass = self.roll_pass()

    if "roll_force" not in roll_pass.__dict__:
        radius = self.nominal_radius
    else:

        radius = roll_pass.roll.flattening_ratio * roll_pass.roll.nominal_radius
        log.info(f"Calculated a roll radius of {radius * 1e3:.2f} mm using Hitchcook's model!")

    return radius


@RollPass.Roll.max_radius
def max_radius(self: RollPass.Roll):
    if self.has_value("flattened_radius"):
        radius = self.flattened_radius
        return radius


@RollPass.Roll.min_radius
def min_radius(self: RollPass.Roll):
    if self.has_value("flattened_radius"):
        radius = self.flattened_radius - self.groove.depth
        return radius


@RollPass.Roll.working_radius
def working_radius(self: RollPass.Roll):
    if self.has_value("flattened_radius"):
        radius = self.flattened_radius - self.groove.cross_section.centroid.y
        return radius
