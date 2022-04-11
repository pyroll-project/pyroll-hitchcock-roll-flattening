import numpy as np
import logging
from pyroll import RollPass

log = logging.getLogger(__name__)


@RollPass.hookimpl
def roll_poissons_ratio(roll_pass):
    return 0.3


@RollPass.hookimpl
def roll_youngs_modulus(roll_pass):
    return 210000


@RollPass.hookimpl
def nominal_radius_flattened_radius_ratio(roll_pass):
    ratio =

    if ratio <= 5.235:
        return 1 + 16 / np.pi * (1 - roll_pass.roll_poissons_ratio ^ 2) / roll_pass.roll_youngs_modulus * roll_pass.roll_force / (
                roll_pass.in_profile.equivalent_rectangle.height * roll_pass.gap)
    else:
        return (16 / np.pi * (1 - roll_pass.roll_poissons_ratio ^ 2) / roll_pass.roll_youngs_modulus * roll_pass.roll_force / (
                roll_pass.in_profile.equivalent_rectangle.height * roll_pass.gap)) ** (2 / 3)


@RollPass.hookimpl
def previous_roll_force(roll_pass):


@RollPass.hookimpl
def previous_nominal_roll_radius(roll_pass):



@RollPass.hookimpl
def nominal_roll_radius(roll_pass):
    return roll_pass.nominal_radius_flattened_radius_ratio * roll_pass.nominal_roll_radius

