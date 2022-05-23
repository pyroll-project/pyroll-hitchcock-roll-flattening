from pyroll.core import RollPass, Roll


@Roll.hookspec
def poissons_ratio(roll: Roll):
    """Poissions ratio of the roll material."""


@Roll.hookspec
def youngs_modulus(roll: Roll):
    """Elastic modulus of the roll material."""


@RollPass.Roll.hookspec
def flattening_ratio(roll: RollPass.Roll, roll_pass: RollPass):
    """The ratio between flattened and nominal radius of the roll."""


@RollPass.Roll.hookspec
def flattened_radius(roll: Roll, roll_pass: RollPass):
    """Flattened roll radius"""
