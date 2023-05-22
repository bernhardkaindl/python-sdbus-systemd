# SPDX-License-Identifier: LGPL-2.1-or-later
from __future__ import annotations

from typing import Optional

from sdbus.sd_bus_internals import SdBus

from .interfaces import SystemdInterface, SystemdUnitInterface

SYSTEMD_SERVICE_NAME = 'org.freedesktop.systemd1'


class Systemd(SystemdInterface):
    """Systemd object, implements :py:class:`SystemdInterface`"""

    def __init__(self, bus: Optional[SdBus] = None) -> None:
        """
        :param bus: pass the system bus (or set default bus to the system bus)
        """
        super().__init__(SYSTEMD_SERVICE_NAME,
                         '/org/freedesktop/systemd1',
                         bus)

    def get_unit_obj(self, name: str) -> SystemdUnit:
        object_path = self.get_unit(name)
        return SystemdUnit(object_path, self._attached_bus)

    def load_unit_obj(self, name: str) -> SystemdUnit:
        object_path = self.load_unit(name)
        return SystemdUnit(object_path, self._attached_bus)


class SystemdUnit(SystemdUnitInterface):
    """Systemd unit object, implements :py:class:`SystemdUnitInterface`"""

    def __init__(self, object_path: str, bus: Optional[SdBus] = None):
        """
        :param object_path: D-Bus path to systemd unit object
        :param bus: pass the system bus (or set default bus to the system bus)
        """
        super().__init__(SYSTEMD_SERVICE_NAME,
                         object_path,
                         bus)

