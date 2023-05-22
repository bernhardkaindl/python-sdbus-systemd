# SPDX-License-Identifier: LGPL-2.1-or-later
from typing import Optional

from sdbus.sd_bus_internals import SdBus

from .interfaces import SystemdInterfaceAsync


class Systemd(SystemdInterfaceAsync):
    """Systemd object, implements :py:class:`SystemdInterfaceAsync`"""

    def __init__(self, bus: Optional[SdBus] = None) -> None:
        """
        :param bus: pass the system bus (or set default bus to the system bus)
        """
        super().__init__()
        self._connect('org.freedesktop.systemd1', '/org/freedesktop/systemd1', bus)
