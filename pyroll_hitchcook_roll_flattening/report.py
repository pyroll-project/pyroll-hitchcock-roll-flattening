from pyroll import RollPass
from pyroll.ui.report import Report
from pyroll.utils import applies_to_unit_types

@Report.hookimpl
@applies_to_unit_types(RollPass)
def unit_properties(unit: RollPass):
    return dict(
        work_roll_youngs_modulus=f"{unit.roll_youngs_modulus}",
        work_roll_poissions_ratio=f"{unit.roll_poissons_ratio}",
        flattened_roll_ratio=f"{unit.nominal_roll_radius:.4f}"
    )
