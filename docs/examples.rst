Examples
==================

Restarting units
----------------

.. code-block:: python
    import asyncio

    import sdbus
    from sdbus_async.systemd import Systemd

        system_bus = sd_bus_open_system()  # We need system bus
    async def print_and_restart_unit(systemd: Systemd, unit: str) -> None:
        """Example function to get and restart a unit"""
        print(await systemd.get_unit(unit))
        print(await systemd.restart_unit(unit, "replace"))


    if __name__ == "__main__":
        systemd = Systemd(sdbus.sd_bus_open_system())
        asyncio.run(print_and_restart_unit(systemd, "cron.service"))