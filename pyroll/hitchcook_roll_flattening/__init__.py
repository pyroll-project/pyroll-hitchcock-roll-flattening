from pyroll.core import RollPass, Roll
from pyroll.ui import Reporter

from . import specs

Roll.plugin_manager.add_hookspecs(specs)
RollPass.Roll.plugin_manager.add_hookspecs(specs)

from . import impls

Roll.plugin_manager.register(impls)
RollPass.Roll.plugin_manager.register(impls)

from . import report

Reporter.plugin_manager.register(report)
