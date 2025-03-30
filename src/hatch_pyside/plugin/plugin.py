#  SPDX-FileCopyrightText: 2025-present s-ball <s-ball@laposte.net>
#  #
#  SPDX-License-Identifier: MIT
from typing import Any

from hatchling.builders.hooks.plugin.interface import BuildHookInterface
from ..build import build, clean

class PysideBuildHook(BuildHookInterface):
    PLUGIN_NAME = 'pyside'

    def clean(self, _versions: list[str]) -> None:
        clean(self.root)

    def initialize(self, version: str, build_data: dict[str, Any]) -> None:
        build(self.root)
        build_data['artifacts'].append('ui_*.py')