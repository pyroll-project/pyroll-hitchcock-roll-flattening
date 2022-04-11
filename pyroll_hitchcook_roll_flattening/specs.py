from pyroll import RollPass


@RollPass.hookspec
def roll_poissons_ratio(roll_pass):
    """Poissions ratio of the roll material."""


@RollPass.hookspec
def roll_youngs_modulus(roll_pass):
    """Youngs modulus of the roll material."""


@RollPass.hookimpl
def previous_roll_force(roll_pass):
    """Roll force of previous iteration step"""


@RollPass.hookimpl
def previous_nominal_roll_radius(roll_pass):
    """Nominal roll radius of previous iteration step"""


@RollPass.hookspec
def nominal_radius_flattened_radius_ratio(roll_pass):
    """Calculate the ratio between nominal radius and flattened radius of roll."""
