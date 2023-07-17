# SPDX-License-Identifier: LGPL-2.1-or-later
from __future__ import annotations

from typing import Any, List, Tuple

from sdbus import (
    DbusInterfaceCommonAsync,
    DbusPropertyConstFlag,
    DbusPropertyEmitsInvalidationFlag,
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


class SystemdServiceInterfaceAsync(
    DbusInterfaceCommonAsync,
    interface_name='org.freedesktop.systemd1.Service',
):
    @dbus_method_async(
        result_signature='a(sus)',
    )
    async def get_processes(
        self,
    ) -> List[Tuple[str, int, str]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='sau',
    )
    async def attach_processes(
        self,
        subcgroup: str,
        pids: List[int],
    ) -> None:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def type(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def restart(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def p_i_d_file(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def notify_access(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def restart_u_sec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def timeout_start_u_sec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def timeout_stop_u_sec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def timeout_abort_u_sec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def timeout_start_failure_mode(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def timeout_stop_failure_mode(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def runtime_max_u_sec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def watchdog_u_sec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def watchdog_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def watchdog_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def root_directory_start_only(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def remain_after_exit(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def guess_main_p_i_d(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='(aiai)',
        flags=DbusPropertyConstFlag,
    )
    def restart_prevent_exit_status(self) -> Tuple[List[int], List[int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='(aiai)',
        flags=DbusPropertyConstFlag,
    )
    def restart_force_exit_status(self) -> Tuple[List[int], List[int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='(aiai)',
        flags=DbusPropertyConstFlag,
    )
    def success_exit_status(self) -> Tuple[List[int], List[int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='u',
    )
    def main_p_i_d(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='u',
    )
    def control_p_i_d(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def bus_name(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='u',
        flags=DbusPropertyConstFlag,
    )
    def file_descriptor_store_max(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='u',
    )
    def n_file_descriptor_store(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def status_text(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='i',
    )
    def status_errno(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def result(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def reload_result(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def clean_result(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def u_s_b_function_descriptors(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def u_s_b_function_strings(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='u',
    )
    def u_i_d(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='u',
    )
    def g_i_d(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='u',
    )
    def n_restarts(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def o_o_m_policy(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def exec_main_start_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def exec_main_start_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def exec_main_exit_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def exec_main_exit_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='u',
    )
    def exec_main_p_i_d(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='i',
    )
    def exec_main_code(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='i',
    )
    def exec_main_status(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(sasbttttuii)',
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def exec_condition(self) -> List[Tuple[str, List[str], bool, int, int, int, int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(sasasttttuii)',
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def exec_condition_ex(self) -> List[Tuple[str, List[str], List[str], int, int, int, int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(sasbttttuii)',
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def exec_start_pre(self) -> List[Tuple[str, List[str], bool, int, int, int, int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(sasasttttuii)',
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def exec_start_pre_ex(self) -> List[Tuple[str, List[str], List[str], int, int, int, int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(sasbttttuii)',
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def exec_start(self) -> List[Tuple[str, List[str], bool, int, int, int, int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(sasasttttuii)',
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def exec_start_ex(self) -> List[Tuple[str, List[str], List[str], int, int, int, int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(sasbttttuii)',
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def exec_start_post(self) -> List[Tuple[str, List[str], bool, int, int, int, int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(sasasttttuii)',
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def exec_start_post_ex(self) -> List[Tuple[str, List[str], List[str], int, int, int, int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(sasbttttuii)',
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def exec_reload(self) -> List[Tuple[str, List[str], bool, int, int, int, int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(sasasttttuii)',
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def exec_reload_ex(self) -> List[Tuple[str, List[str], List[str], int, int, int, int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(sasbttttuii)',
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def exec_stop(self) -> List[Tuple[str, List[str], bool, int, int, int, int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(sasasttttuii)',
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def exec_stop_ex(self) -> List[Tuple[str, List[str], List[str], int, int, int, int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(sasbttttuii)',
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def exec_stop_post(self) -> List[Tuple[str, List[str], bool, int, int, int, int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(sasasttttuii)',
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def exec_stop_post_ex(self) -> List[Tuple[str, List[str], List[str], int, int, int, int, int, int, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def slice(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def control_group(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def memory_current(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def c_p_u_usage_n_sec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='ay',
    )
    def effective_c_p_us(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='ay',
    )
    def effective_memory_nodes(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def tasks_current(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def i_p_ingress_bytes(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def i_p_ingress_packets(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def i_p_egress_bytes(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def i_p_egress_packets(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def i_o_read_bytes(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def i_o_read_operations(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def i_o_write_bytes(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def i_o_write_operations(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def delegate(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
    )
    def delegate_controllers(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def c_p_u_accounting(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def c_p_u_weight(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def startup_c_p_u_weight(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def c_p_u_shares(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def startup_c_p_u_shares(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def c_p_u_quota_per_sec_u_sec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def c_p_u_quota_period_u_sec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='ay',
    )
    def allowed_c_p_us(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='ay',
    )
    def allowed_memory_nodes(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def i_o_accounting(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def i_o_weight(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def startup_i_o_weight(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(st)',
    )
    def i_o_device_weight(self) -> List[Tuple[str, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(st)',
    )
    def i_o_read_bandwidth_max(self) -> List[Tuple[str, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(st)',
    )
    def i_o_write_bandwidth_max(self) -> List[Tuple[str, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(st)',
    )
    def i_o_read_i_o_p_s_max(self) -> List[Tuple[str, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(st)',
    )
    def i_o_write_i_o_p_s_max(self) -> List[Tuple[str, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(st)',
    )
    def i_o_device_latency_target_u_sec(self) -> List[Tuple[str, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def block_i_o_accounting(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def block_i_o_weight(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def startup_block_i_o_weight(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(st)',
    )
    def block_i_o_device_weight(self) -> List[Tuple[str, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(st)',
    )
    def block_i_o_read_bandwidth(self) -> List[Tuple[str, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(st)',
    )
    def block_i_o_write_bandwidth(self) -> List[Tuple[str, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def memory_accounting(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def default_memory_low(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def default_memory_min(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def memory_min(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def memory_low(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def memory_high(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def memory_max(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def memory_swap_max(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def memory_limit(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def device_policy(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(ss)',
    )
    def device_allow(self) -> List[Tuple[str, str]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def tasks_accounting(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def tasks_max(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def i_p_accounting(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(iayu)',
    )
    def i_p_address_allow(self) -> List[Tuple[int, bytes, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(iayu)',
    )
    def i_p_address_deny(self) -> List[Tuple[int, bytes, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
    )
    def i_p_ingress_filter_path(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
    )
    def i_p_egress_filter_path(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
    )
    def disable_controllers(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def managed_o_o_m_swap(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def managed_o_o_m_memory_pressure(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def managed_o_o_m_memory_pressure_limit_percent(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def environment(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(sb)',
        flags=DbusPropertyConstFlag,
    )
    def environment_files(self) -> List[Tuple[str, bool]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def pass_environment(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def unset_environment(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='u',
        flags=DbusPropertyConstFlag,
    )
    def u_mask(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_c_p_u(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_c_p_u_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_f_s_i_z_e(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_f_s_i_z_e_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_d_a_t_a(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_d_a_t_a_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_s_t_a_c_k(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_s_t_a_c_k_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_c_o_r_e(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_c_o_r_e_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_r_s_s(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_r_s_s_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_n_o_f_i_l_e(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_n_o_f_i_l_e_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_a_s(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_a_s_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_n_p_r_o_c(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_n_p_r_o_c_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_m_e_m_l_o_c_k(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_m_e_m_l_o_c_k_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_l_o_c_k_s(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_l_o_c_k_s_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_s_i_g_p_e_n_d_i_n_g(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_s_i_g_p_e_n_d_i_n_g_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_m_s_g_q_u_e_u_e(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_m_s_g_q_u_e_u_e_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_n_i_c_e(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_n_i_c_e_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_r_t_p_r_i_o(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_r_t_p_r_i_o_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_r_t_t_i_m_e(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def limit_r_t_t_i_m_e_soft(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def working_directory(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def root_directory(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def root_image(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(ss)',
        flags=DbusPropertyConstFlag,
    )
    def root_image_options(self) -> List[Tuple[str, str]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='ay',
        flags=DbusPropertyConstFlag,
    )
    def root_hash(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def root_hash_path(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='ay',
        flags=DbusPropertyConstFlag,
    )
    def root_hash_signature(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def root_hash_signature_path(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def root_verity(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(ssba(ss))',
        flags=DbusPropertyConstFlag,
    )
    def mount_images(self) -> List[Tuple[str, str, bool, List[Tuple[str, str]]]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='i',
        flags=DbusPropertyConstFlag,
    )
    def o_o_m_score_adjust(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def coredump_filter(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='i',
        flags=DbusPropertyConstFlag,
    )
    def nice(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='i',
        flags=DbusPropertyConstFlag,
    )
    def i_o_scheduling_class(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='i',
        flags=DbusPropertyConstFlag,
    )
    def i_o_scheduling_priority(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='i',
        flags=DbusPropertyConstFlag,
    )
    def c_p_u_scheduling_policy(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='i',
        flags=DbusPropertyConstFlag,
    )
    def c_p_u_scheduling_priority(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='ay',
        flags=DbusPropertyConstFlag,
    )
    def c_p_u_affinity(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def c_p_u_affinity_from_n_u_m_a(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='i',
        flags=DbusPropertyConstFlag,
    )
    def n_u_m_a_policy(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='ay',
        flags=DbusPropertyConstFlag,
    )
    def n_u_m_a_mask(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def timer_slack_n_sec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def c_p_u_scheduling_reset_on_fork(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def non_blocking(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def standard_input(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def standard_input_file_descriptor_name(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='ay',
        flags=DbusPropertyConstFlag,
    )
    def standard_input_data(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def standard_output(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def standard_output_file_descriptor_name(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def standard_error(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def standard_error_file_descriptor_name(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def t_t_y_path(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def t_t_y_reset(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def t_t_y_v_hangup(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def t_t_y_v_t_disallocate(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='i',
        flags=DbusPropertyConstFlag,
    )
    def syslog_priority(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def syslog_identifier(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def syslog_level_prefix(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='i',
        flags=DbusPropertyConstFlag,
    )
    def syslog_level(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='i',
        flags=DbusPropertyConstFlag,
    )
    def syslog_facility(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='i',
        flags=DbusPropertyConstFlag,
    )
    def log_level_max(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def log_rate_limit_interval_u_sec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='u',
        flags=DbusPropertyConstFlag,
    )
    def log_rate_limit_burst(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='aay',
        flags=DbusPropertyConstFlag,
    )
    def log_extra_fields(self) -> List[bytes]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def log_namespace(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='i',
        flags=DbusPropertyConstFlag,
    )
    def secure_bits(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def capability_bounding_set(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def ambient_capabilities(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def user(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def group(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def dynamic_user(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def remove_i_p_c(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(say)',
        flags=DbusPropertyConstFlag,
    )
    def set_credential(self) -> List[Tuple[str, bytes]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(ss)',
        flags=DbusPropertyConstFlag,
    )
    def load_credential(self) -> List[Tuple[str, str]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def supplementary_groups(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def p_a_m_name(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def read_write_paths(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def read_only_paths(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def inaccessible_paths(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def mount_flags(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def private_tmp(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def private_devices(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def protect_clock(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def protect_kernel_tunables(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def protect_kernel_modules(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def protect_kernel_logs(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def protect_control_groups(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def private_network(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def private_users(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def private_mounts(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def protect_home(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def protect_system(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def same_process_group(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def utmp_identifier(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def utmp_mode(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='(bs)',
        flags=DbusPropertyConstFlag,
    )
    def s_e_linux_context(self) -> Tuple[bool, str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='(bs)',
        flags=DbusPropertyConstFlag,
    )
    def app_armor_profile(self) -> Tuple[bool, str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='(bs)',
        flags=DbusPropertyConstFlag,
    )
    def smack_process_label(self) -> Tuple[bool, str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def ignore_s_i_g_p_i_p_e(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def no_new_privileges(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='(bas)',
        flags=DbusPropertyConstFlag,
    )
    def system_call_filter(self) -> Tuple[bool, List[str]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def system_call_architectures(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='i',
        flags=DbusPropertyConstFlag,
    )
    def system_call_error_number(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='(bas)',
        flags=DbusPropertyConstFlag,
    )
    def system_call_log(self) -> Tuple[bool, List[str]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def personality(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def lock_personality(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='(bas)',
        flags=DbusPropertyConstFlag,
    )
    def restrict_address_families(self) -> Tuple[bool, List[str]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def runtime_directory_preserve(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='u',
        flags=DbusPropertyConstFlag,
    )
    def runtime_directory_mode(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def runtime_directory(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='u',
        flags=DbusPropertyConstFlag,
    )
    def state_directory_mode(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def state_directory(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='u',
        flags=DbusPropertyConstFlag,
    )
    def cache_directory_mode(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def cache_directory(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='u',
        flags=DbusPropertyConstFlag,
    )
    def logs_directory_mode(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def logs_directory(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='u',
        flags=DbusPropertyConstFlag,
    )
    def configuration_directory_mode(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def configuration_directory(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def timeout_clean_u_sec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def memory_deny_write_execute(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def restrict_realtime(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def restrict_s_u_i_d_s_g_i_d(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def restrict_namespaces(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(ssbt)',
        flags=DbusPropertyConstFlag,
    )
    def bind_paths(self) -> List[Tuple[str, str, bool, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(ssbt)',
        flags=DbusPropertyConstFlag,
    )
    def bind_read_only_paths(self) -> List[Tuple[str, str, bool, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(ss)',
        flags=DbusPropertyConstFlag,
    )
    def temporary_file_system(self) -> List[Tuple[str, str]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def mount_a_p_i_v_f_s(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def keyring_mode(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def protect_proc(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def proc_subset(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def protect_hostname(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def network_namespace_path(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def kill_mode(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='i',
        flags=DbusPropertyConstFlag,
    )
    def kill_signal(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='i',
        flags=DbusPropertyConstFlag,
    )
    def restart_kill_signal(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='i',
        flags=DbusPropertyConstFlag,
    )
    def final_kill_signal(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def send_s_i_g_k_i_l_l(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def send_s_i_g_h_u_p(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='i',
        flags=DbusPropertyConstFlag,
    )
    def watchdog_signal(self) -> int:
        raise NotImplementedError


class SystemdUnitInterfaceAsync(
    DbusInterfaceCommonAsync,
    interface_name='org.freedesktop.systemd1.Unit',
):
    @dbus_method_async(
        input_signature='s',
        result_signature='o',
    )
    async def start(
        self,
        mode: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
        result_signature='o',
    )
    async def stop(
        self,
        mode: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
        result_signature='o',
    )
    async def reload(
        self,
        mode: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
        result_signature='o',
    )
    async def restart(
        self,
        mode: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
        result_signature='o',
    )
    async def try_restart(
        self,
        mode: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
        result_signature='o',
    )
    async def reload_or_restart(
        self,
        mode: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='s',
        result_signature='o',
    )
    async def reload_or_try_restart(
        self,
        mode: str,
    ) -> str:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='ss',
        result_signature='uososa(uosos)',
    )
    async def enqueue_job(
        self,
        job_type: str,
        job_mode: str,
    ) -> Tuple[int, str, str, str, str, List[Tuple[int, str, str, str, str]]]:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='si',
    )
    async def kill(
        self,
        whom: str,
        signal: int,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async()
    async def reset_failed(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='ba(sv)',
    )
    async def set_properties(
        self,
        runtime: bool,
        properties: List[Tuple[str, Tuple[str, Any]]],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async()
    async def ref(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async()
    async def unref(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async(
        input_signature='as',
    )
    async def clean(
        self,
        mask: List[str],
    ) -> None:
        raise NotImplementedError

    @dbus_method_async()
    async def freeze(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_method_async()
    async def thaw(
        self,
    ) -> None:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def id(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def names(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def following(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def requires(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def requisite(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def wants(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def binds_to(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def part_of(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def required_by(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def requisite_of(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def wanted_by(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def bound_by(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def consists_of(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def conflicts(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def conflicted_by(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def before(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def after(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def on_failure(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def on_failure_of(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def on_success(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def on_success_of(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def triggers(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def triggered_by(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def propagates_reload_to(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def reload_propagated_from(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def propagates_stop_to(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def stop_propagated_from(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def joins_namespace_of(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def slice_of(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def requires_mounts_for(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def documentation(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def description(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def load_state(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def active_state(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def freezer_state(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def sub_state(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def fragment_path(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def source_path(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def drop_in_paths(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def unit_file_state(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
    )
    def unit_file_preset(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def state_change_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def state_change_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def inactive_exit_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def inactive_exit_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def active_enter_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def active_enter_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def active_exit_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def active_exit_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def inactive_enter_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def inactive_enter_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def can_start(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def can_stop(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def can_reload(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def can_isolate(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
        flags=DbusPropertyConstFlag,
    )
    def can_clean(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def can_freeze(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='(uo)',
    )
    def job(self) -> Tuple[int, str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def stop_when_unneeded(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def refuse_manual_start(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def refuse_manual_stop(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def allow_isolate(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def default_dependencies(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def on_success_job_mode(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def on_failure_job_mode(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def ignore_on_isolate(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def need_daemon_reload(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
    )
    def markers(self) -> List[str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def job_timeout_u_sec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def job_running_timeout_u_sec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def job_timeout_action(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def job_timeout_reboot_argument(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def condition_result(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
    )
    def assert_result(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def condition_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def condition_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def assert_timestamp(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
    )
    def assert_timestamp_monotonic(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(sbbsi)',
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def conditions(self) -> List[Tuple[str, bool, bool, str, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='a(sbbsi)',
        flags=DbusPropertyEmitsInvalidationFlag,
    )
    def asserts(self) -> List[Tuple[str, bool, bool, str, int]]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='(ss)',
        flags=DbusPropertyConstFlag,
    )
    def load_error(self) -> Tuple[str, str]:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def transient(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='b',
        flags=DbusPropertyConstFlag,
    )
    def perpetual(self) -> bool:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='t',
        flags=DbusPropertyConstFlag,
    )
    def start_limit_interval_u_sec(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='u',
        flags=DbusPropertyConstFlag,
    )
    def start_limit_burst(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def start_limit_action(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def failure_action(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='i',
        flags=DbusPropertyConstFlag,
    )
    def failure_action_exit_status(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def success_action(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='i',
        flags=DbusPropertyConstFlag,
    )
    def success_action_exit_status(self) -> int:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def reboot_argument(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='ay',
    )
    def invocation_i_d(self) -> bytes:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='s',
        flags=DbusPropertyConstFlag,
    )
    def collect_mode(self) -> str:
        raise NotImplementedError

    @dbus_property_async(
        property_signature='as',
    )
    def refs(self) -> List[str]:
        raise NotImplementedError
