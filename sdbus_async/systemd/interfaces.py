# SPDX-License-Identifier: LGPL-2.1-or-later
from __future__ import annotations

from typing import Any, List, Tuple

from sdbus import (
    DbusInterfaceCommonAsync,
    DbusPropertyConstFlag,
    DbusUnprivilegedFlag,
    dbus_method_async,
    dbus_property_async,
    dbus_signal_async,
)


class SystemdInterfaceAsync(
    DbusInterfaceCommonAsync,
    interface_name='org.freedesktop.systemd1.Manager',
):
    @dbus_method_async(
        input_signature='s',
        result_signature='o',
    )
    async def get_unit(
        self,
        name: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='u',
        result_signature='o',
    )
    async def get_unit_by_p_i_d(
        self,
        pid: int,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='ay',
        result_signature='o',
    )
    async def get_unit_by_invocation_i_d(
        self,
        invocation_id: bytes,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
        result_signature='o',
    )
    async def get_unit_by_control_group(
        self,
        cgroup: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
        result_signature='o',
    )
    async def load_unit(
        self,
        name: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='ss',
        result_signature='o',
    )
    async def start_unit(
        self,
        name: str,
        mode: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='sss',
        result_signature='o',
    )
    async def start_unit_replace(
        self,
        old_unit: str,
        new_unit: str,
        mode: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='ss',
        result_signature='o',
    )
    async def stop_unit(
        self,
        name: str,
        mode: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='ss',
        result_signature='o',
    )
    async def reload_unit(
        self,
        name: str,
        mode: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='ss',
        result_signature='o',
    )
    async def restart_unit(
        self,
        name: str,
        mode: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='ss',
        result_signature='o',
    )
    async def try_restart_unit(
        self,
        name: str,
        mode: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='ss',
        result_signature='o',
    )
    async def reload_or_restart_unit(
        self,
        name: str,
        mode: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='ss',
        result_signature='o',
    )
    async def reload_or_try_restart_unit(
        self,
        name: str,
        mode: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='sss',
        result_signature='uososa(uosos)',
    )
    async def enqueue_unit_job(
        self,
        name: str,
        job_type: str,
        job_mode: str,
    ) -> Tuple[int, str, str, str, str, List[Tuple[int, str, str, str, str]]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='ssi',
    )
    async def kill_unit(
        self,
        name: str,
        whom: str,
        signal: int,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='sas',
    )
    async def clean_unit(
        self,
        name: str,
        mask: List[str],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
    )
    async def freeze_unit(
        self,
        name: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
    )
    async def thaw_unit(
        self,
        name: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
    )
    async def reset_failed_unit(
        self,
        name: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='sba(sv)',
    )
    async def set_unit_properties(
        self,
        name: str,
        runtime: bool,
        properties: List[Tuple[str, Tuple[str, Any]]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
    )
    async def ref_unit(
        self,
        name: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
    )
    async def unref_unit(
        self,
        name: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='ssa(sv)a(sa(sv))',
        result_signature='o',
    )
    async def start_transient_unit(
        self,
        name: str,
        mode: str,
        properties: List[Tuple[str, Tuple[str, Any]]],
        aux: List[Tuple[str, List[Tuple[str, Tuple[str, Any]]]]],
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
        result_signature='a(sus)',
    )
    async def get_unit_processes(
        self,
        name: str,
    ) -> List[Tuple[str, int, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='ssau',
    )
    async def attach_processes_to_unit(
        self,
        unit_name: str,
        subcgroup: str,
        pids: List[int],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
    )
    async def abandon_scope(
        self,
        name: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='u',
        result_signature='o',
    )
    async def get_job(
        self,
        id: int,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='u',
        result_signature='a(usssoo)',
    )
    async def get_job_after(
        self,
        id: int,
    ) -> List[Tuple[int, str, str, str, str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='u',
        result_signature='a(usssoo)',
    )
    async def get_job_before(
        self,
        id: int,
    ) -> List[Tuple[int, str, str, str, str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='u',
    )
    async def cancel_job(
        self,
        id: int,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async()
    async def clear_jobs(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async()
    async def reset_failed(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
        flags=DbusUnprivilegedFlag,
    )
    async def set_show_status(
        self,
        mode: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        result_signature='a(ssssssouso)',
    )
    async def list_units(
        self,
    ) -> List[Tuple[str, str, str, str, str, str, str, int, str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='as',
        result_signature='a(ssssssouso)',
    )
    async def list_units_filtered(
        self,
        states: List[str],
    ) -> List[Tuple[str, str, str, str, str, str, str, int, str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='asas',
        result_signature='a(ssssssouso)',
    )
    async def list_units_by_patterns(
        self,
        states: List[str],
        patterns: List[str],
    ) -> List[Tuple[str, str, str, str, str, str, str, int, str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='as',
        result_signature='a(ssssssouso)',
    )
    async def list_units_by_names(
        self,
        names: List[str],
    ) -> List[Tuple[str, str, str, str, str, str, str, int, str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        result_signature='a(usssoo)',
    )
    async def list_jobs(
        self,
    ) -> List[Tuple[int, str, str, str, str, str]]:
        raise NotImplementedError

    @dbus_method_async()
    async def subscribe(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async()
    async def unsubscribe(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        result_signature='s',
    )
    async def dump(
        self,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        result_signature='h',
    )
    async def dump_by_file_descriptor(
        self,
    ) -> int:
        raise NotImplementedError

    @dbus_method_async()
    async def reload(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async()
    async def reexecute(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        flags=DbusUnprivilegedFlag,
    )
    async def exit(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        flags=DbusUnprivilegedFlag,
    )
    async def reboot(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        flags=DbusUnprivilegedFlag,
    )
    async def power_off(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        flags=DbusUnprivilegedFlag,
    )
    async def halt(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        flags=DbusUnprivilegedFlag,
    )
    async def k_exec(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='ss',
        flags=DbusUnprivilegedFlag,
    )
    async def switch_root(
        self,
        new_root: str,
        init: str,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='as',
    )
    async def set_environment(
        self,
        assignments: List[str],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='as',
    )
    async def unset_environment(
        self,
        names: List[str],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='asas',
    )
    async def unset_and_set_environment(
        self,
        names: List[str],
        assignments: List[str],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        result_signature='a(ss)',
    )
    async def list_unit_files(
        self,
    ) -> List[Tuple[str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='asas',
        result_signature='a(ss)',
    )
    async def list_unit_files_by_patterns(
        self,
        states: List[str],
        patterns: List[str],
    ) -> List[Tuple[str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
        result_signature='s',
    )
    async def get_unit_file_state(
        self,
        file: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='asbb',
        result_signature='ba(sss)',
    )
    async def enable_unit_files(
        self,
        files: List[str],
        runtime: bool,
        force: bool,
    ) -> Tuple[bool, List[Tuple[str, str, str]]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='asb',
        result_signature='a(sss)',
    )
    async def disable_unit_files(
        self,
        files: List[str],
        runtime: bool,
    ) -> List[Tuple[str, str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='ast',
        result_signature='ba(sss)',
    )
    async def enable_unit_files_with_flags(
        self,
        files: List[str],
        flags: int,
    ) -> Tuple[bool, List[Tuple[str, str, str]]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='ast',
        result_signature='a(sss)',
    )
    async def disable_unit_files_with_flags(
        self,
        files: List[str],
        flags: int,
    ) -> List[Tuple[str, str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='asbb',
        result_signature='ba(sss)',
    )
    async def reenable_unit_files(
        self,
        files: List[str],
        runtime: bool,
        force: bool,
    ) -> Tuple[bool, List[Tuple[str, str, str]]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='asbb',
        result_signature='a(sss)',
    )
    async def link_unit_files(
        self,
        files: List[str],
        runtime: bool,
        force: bool,
    ) -> List[Tuple[str, str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='asbb',
        result_signature='ba(sss)',
    )
    async def preset_unit_files(
        self,
        files: List[str],
        runtime: bool,
        force: bool,
    ) -> Tuple[bool, List[Tuple[str, str, str]]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='assbb',
        result_signature='ba(sss)',
    )
    async def preset_unit_files_with_mode(
        self,
        files: List[str],
        mode: str,
        runtime: bool,
        force: bool,
    ) -> Tuple[bool, List[Tuple[str, str, str]]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='asbb',
        result_signature='a(sss)',
    )
    async def mask_unit_files(
        self,
        files: List[str],
        runtime: bool,
        force: bool,
    ) -> List[Tuple[str, str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='asb',
        result_signature='a(sss)',
    )
    async def unmask_unit_files(
        self,
        files: List[str],
        runtime: bool,
    ) -> List[Tuple[str, str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='as',
        result_signature='a(sss)',
    )
    async def revert_unit_files(
        self,
        files: List[str],
    ) -> List[Tuple[str, str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='sb',
        result_signature='a(sss)',
    )
    async def set_default_target(
        self,
        name: str,
        force: bool,
    ) -> List[Tuple[str, str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        result_signature='s',
    )
    async def get_default_target(
        self,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='sbb',
        result_signature='a(sss)',
    )
    async def preset_all_unit_files(
        self,
        mode: str,
        runtime: bool,
        force: bool,
    ) -> List[Tuple[str, str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='asssbb',
        result_signature='a(sss)',
    )
    async def add_dependency_unit_files(
        self,
        files: List[str],
        target: str,
        type: str,
        runtime: bool,
        force: bool,
    ) -> List[Tuple[str, str, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='sb',
        result_signature='as',
    )
    async def get_unit_file_links(
        self,
        name: str,
        runtime: bool,
    ) -> List[str]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='y',
    )
    async def set_exit_code(
        self,
        number: int,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
        result_signature='u',
    )
    async def lookup_dynamic_user_by_name(
        self,
        name: str,
    ) -> int:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='u',
        result_signature='s',
    )
    async def lookup_dynamic_user_by_u_i_d(
        self,
        uid: int,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        result_signature='a(us)',
    )
    async def get_dynamic_users(
        self,
    ) -> List[Tuple[int, str]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def version(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def features(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def virtualization(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def architecture(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def tainted(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def firmware_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def firmware_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def loader_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def loader_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def kernel_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def kernel_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def init_r_d_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def init_r_d_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def userspace_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def userspace_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def finish_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def finish_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def security_start_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def security_start_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def security_finish_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def security_finish_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def generators_start_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def generators_start_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def generators_finish_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def generators_finish_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def units_load_start_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def units_load_start_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def units_load_finish_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def units_load_finish_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def init_r_d_security_start_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def init_r_d_security_start_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def init_r_d_security_finish_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def init_r_d_security_finish_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def init_r_d_generators_start_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def init_r_d_generators_start_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def init_r_d_generators_finish_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def init_r_d_generators_finish_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def init_r_d_units_load_start_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def init_r_d_units_load_start_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def init_r_d_units_load_finish_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def init_r_d_units_load_finish_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusUnprivilegedFlag,
    )
    def log_level(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusUnprivilegedFlag,
    )
    def log_target(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='u',
    )
    def n_names(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='u',
    )
    def n_failed_units(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='u',
    )
    def n_jobs(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='u',
    )
    def n_installed_jobs(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='u',
    )
    def n_failed_jobs(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='d',
    )
    def progress(self) -> float:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
    )
    def environment(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def confirm_spawn(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def show_status(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def unit_path(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def default_standard_output(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def default_standard_error(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusUnprivilegedFlag,
    )
    def runtime_watchdog_u_sec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusUnprivilegedFlag,
    )
    def reboot_watchdog_u_sec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusUnprivilegedFlag,
    )
    def k_exec_watchdog_u_sec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusUnprivilegedFlag,
    )
    def service_watchdogs(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def control_group(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def system_state(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='y',
    )
    def exit_code(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_timer_accuracy_u_sec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_timeout_start_u_sec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_timeout_stop_u_sec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def default_timeout_abort_u_sec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_restart_u_sec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_start_limit_interval_u_sec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='u',
        flags=DbusPropertyConstFlag,
    )
    def default_start_limit_burst(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def default_c_p_u_accounting(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def default_block_i_o_accounting(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def default_memory_accounting(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def default_tasks_accounting(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_c_p_u(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_c_p_u_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_f_s_i_z_e(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_f_s_i_z_e_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_d_a_t_a(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_d_a_t_a_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_s_t_a_c_k(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_s_t_a_c_k_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_c_o_r_e(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_c_o_r_e_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_r_s_s(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_r_s_s_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_n_o_f_i_l_e(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_n_o_f_i_l_e_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_a_s(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_a_s_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_n_p_r_o_c(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_n_p_r_o_c_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_m_e_m_l_o_c_k(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_m_e_m_l_o_c_k_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_l_o_c_k_s(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_l_o_c_k_s_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_s_i_g_p_e_n_d_i_n_g(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_s_i_g_p_e_n_d_i_n_g_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_m_s_g_q_u_e_u_e(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_m_s_g_q_u_e_u_e_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_n_i_c_e(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_n_i_c_e_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_r_t_p_r_i_o(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_r_t_p_r_i_o_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_r_t_t_i_m_e(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def default_limit_r_t_t_i_m_e_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def default_tasks_max(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def timer_slack_n_sec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def default_o_o_m_policy(self) -> str:
        raise NotImplementedError

    @dbus_signal_async(
        signal_signature='so',
    )
    def unit_new(self) -> Tuple[str, str]:
        raise NotImplementedError

    @dbus_signal_async(
        signal_signature='so',
    )
    def unit_removed(self) -> Tuple[str, str]:
        raise NotImplementedError

    @dbus_signal_async(
        signal_signature='uos',
    )
    def job_new(self) -> Tuple[int, str, str]:
        raise NotImplementedError

    @dbus_signal_async(
        signal_signature='uoss',
    )
    def job_removed(self) -> Tuple[int, str, str, str]:
        raise NotImplementedError

    @dbus_signal_async(
        signal_signature='tttttt',
    )
    def startup_finished(self) -> Tuple[int, int, int, int, int, int]:
        raise NotImplementedError

    @dbus_signal_async()
    def unit_files_changed(self) -> None:
        raise NotImplementedError

    @dbus_signal_async(
        signal_signature='b',
    )
    def reloading(self) -> bool:
        raise NotImplementedError
