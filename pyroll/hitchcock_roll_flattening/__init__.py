from pyroll.core import RollPass, Roll
from pyroll.ui import Reporter

from . import specs
from . import impls
from . import report

Roll.plugin_manager.add_hookspecs(specs)
RollPass.Roll.plugin_manager.add_hookspecs(specs)

Roll.plugin_manager.register(impls)
RollPass.Roll.plugin_manager.register(impls)

Reporter.plugin_manager.register(report)
