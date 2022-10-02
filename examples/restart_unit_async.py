# SPDX-License-Identifier: LGPL-2.1-or-later
import asyncio

import sdbus
from sdbus_async.systemd import Systemd


async def print_and_restart_unit(systemd: Systemd, unit: str) -> None:
    """Example function to get and restart a unit"""
    print(await systemd.get_unit(unit))
    print(await systemd.restart_unit(unit, "replace"))


if __name__ == "__main__":
    systemd = Systemd(sdbus.sd_bus_open_system())
    asyncio.run(print_and_restart_unit(systemd, "cron.service"))
