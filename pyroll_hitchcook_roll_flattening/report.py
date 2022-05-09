from pyroll import RollPass
from pyroll import Reporter
from pyroll import for_units


@Reporter.hookimpl
@for_units(RollPass)
def unit_properties(unit: RollPass):
    return dict(
        work_roll_elastic_modulus=f"{unit.roll.elastic_modulus}",
        work_roll_poissions_ratio=f"{unit.roll.poissons_ratio}",
        flattened_roll_radius=f"{unit.roll.flattened_radius}"
    )
