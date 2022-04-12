from pyroll import RollPass
from pyroll.ui.report import Report
from pyroll.utils import for_units


@Report.hookimpl
@for_units(RollPass)
def unit_properties(unit: RollPass):
    return dict(
        work_roll_youngs_modulus=f"{unit.roll_youngs_modulus}",
        work_roll_poissions_ratio=f"{unit.roll_poissons_ratio}",
        flattened_roll_radius=f"{unit.flattened_roll_radius}"
    )
