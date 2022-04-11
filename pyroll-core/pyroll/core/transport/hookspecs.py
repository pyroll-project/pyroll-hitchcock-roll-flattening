import sys

from .transport import TransportOutProfile


@TransportOutProfile.hookspec
def strain(transport):
    """Take a transport object and calculate mean temperature.
    Return a dict with at least a "mean_temperature" key.
    This will be used to update the transport.
    First implementation that does not return None is taken.
    Do NOT modify the transport object yourself, since this could result in undefined behavior."""


TransportOutProfile.plugin_manager.add_hookspecs(sys.modules[__name__])
