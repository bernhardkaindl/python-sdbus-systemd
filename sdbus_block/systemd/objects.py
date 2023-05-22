# SPDX-License-Identifier: LGPL-2.1-or-later
from typing import Optional

from sdbus.sd_bus_internals import SdBus

from .interfaces import SystemdInterface


class Systemd(SystemdInterface):
    """Systemd object, implements :py:class:`SystemdInterface`"""

    def __init__(self, bus: Optional[SdBus] = None) -> None:
        """
        :param bus: pass the system bus (or set default bus to the system bus)
        """
        super().__init__('org.freedesktop.systemd1',
                         '/org/freedesktop/systemd1',
                         bus)
