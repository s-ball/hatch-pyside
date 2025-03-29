#  SPDX-FileCopyrightText: 2025-present s-ball <s-ball@laposte.net>
#  #
#  SPDX-License-Identifier: MIT
import shutil
import subprocess
import sysconfig

__all__ = ['command', 'build', 'clean']
command: list[str]


def build(folder: str) -> None:
    subprocess.run(command + ['build', folder])


def clean(folder: str) -> None:
    subprocess.run(command + ['clean', folder])


def _build_command() -> str:
    prog = 'pyside6-project'
    cmd = shutil.which(prog)
    if cmd is None:
        visited = set()
        for d in (sysconfig.get_path('scripts', scheme)
                     for scheme in sysconfig.get_scheme_names()):
            if d in visited:
                continue
            visited.add(d)
            cmd = shutil.which(prog)
            if cmd is not None:
                break
            else:
                raise RuntimeError(f'No installation of {prog} found')
    return cmd


command = [_build_command()]
