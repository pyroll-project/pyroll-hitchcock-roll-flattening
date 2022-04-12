from pyroll import RollPass


@RollPass.hookspec
def roll_poissons_ratio(roll_pass):
    """Poissions ratio of the roll material."""


@RollPass.hookspec
def roll_youngs_modulus(roll_pass):
    """Youngs modulus of the roll material."""


@RollPass.hookimpl
def control_hook(roll_pass):
    """Hook for control of loop """


@RollPass.hookspec
def flattened_radius_nominal_radius_ratio(roll_pass):
    """Calculate the ratio between flattened and nominal radius of roll."""


@RollPass.hookimpl
def flattened_roll_radius(roll_pass):
    """Flattened roll radius"""
