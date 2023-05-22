# SPDX-License-Identifier: LGPL-2.1-or-later
from __future__ import annotations

from typing import Optional

from sdbus.sd_bus_internals import SdBus

from .interfaces import SystemdInterfaceAsync, SystemdUnitInterfaceAsync

SYSTEMD_SERVICE_NAME = 'org.freedesktop.systemd1'


class Systemd(SystemdInterfaceAsync):
    """Systemd object, implements :py:class:`SystemdInterfaceAsync`"""

    def __init__(self, bus: Optional[SdBus] = None) -> None:
        """
        :param bus: pass the system bus (or set default bus to the system bus)
        """
        super().__init__()
        self._connect(SYSTEMD_SERVICE_NAME, '/org/freedesktop/systemd1', bus)

    async def get_unit_obj(self, name: str) -> SystemdUnit:
        object_path = await self.get_unit(name)
        return SystemdUnit(object_path, self._attached_bus)

    async def load_unit_obj(self, name: str) -> SystemdUnit:
        object_path = await self.load_unit(name)
        return SystemdUnit(object_path, self._attached_bus)


class SystemdUnit(SystemdUnitInterfaceAsync):
    """Systemd unit object, implements :py:class:`SystemdUnitInterfaceAsync`"""

    def __init__(self, object_path: str, bus: Optional[SdBus] = None):
        """
        :param object_path: D-Bus path to systemd unit object
        :param bus: pass the system bus (or set default bus to the system bus)
        """
        super().__init__()
        self._connect(SYSTEMD_SERVICE_NAME, object_path, bus)
