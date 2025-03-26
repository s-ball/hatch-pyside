#  SPDX-FileCopyrightText: 2025-present s-ball <s-ball@laposte.net>
#  #
#  SPDX-License-Identifier: MIT
from typing import Any, Optional

try:
    # noinspection PyUnresolvedReferences
    import tomllib
except ImportError:
    # noinspection PyUnresolvedReferences
    import tomli as tomllib


def get_values(cfg: dict[str, Any]) -> Optional[list[str]]:
    try:
        return  cfg['build']['targets']['wheel']['hooks']['pyside']['folders']
    except KeyError:
        return cfg['build']['hooks']['pyside']['folders']


def get_project_folders() -> Optional[list[str]]:
    """ Extract hatch-pyside config from pyproject.toml or hatch.toml """
    try:
        with open('pyproject.toml', 'rb') as fd:
            return get_values(tomllib.load(fd)['tool']['hatch'])
    except KeyError:
        try:
            with open('hatch.toml', 'rb') as fd:
                return get_values(tomllib.load(fd))
        except (OSError, KeyError):
            return None
