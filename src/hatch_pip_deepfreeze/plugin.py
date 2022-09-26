# SPDX-FileCopyrightText: 2022-present Stéphane Bidoul <stephane.bidoul@acsone.eu>
#
# SPDX-License-Identifier: MIT

import sys
from typing import List

from hatch.env.virtual import VirtualEnvironment


class PipDeepfreezeEnvironment(VirtualEnvironment):
    PLUGIN_NAME = "pip-deepfreeze"

    def _pip_df_sync_cmd(self) -> List[str]:
        if self.environment_dependencies:
            raise NotImplementedError(
                "Per environment dependencies are not supported "
                "in pip-deepfreeze environments. "
                "Please use project.optional-dependencies and "
                "tool.hatch.envs.<ENV NAME>.features."
            )
        cmd = [sys.executable, "-m", "pip_deepfreeze", "sync"]
        if self.features:
            cmd += ["--extras", ",".join(self.features)]
        return cmd

    def install_project(self):
        raise NotImplementedError(
            "Project must be installed in dev mode in pip-deepfreeze environments."
        )

    def install_project_dev_mode(self):
        with self.safe_activation():
            self.platform.check_command(self._pip_df_sync_cmd())

    def dependencies_in_sync(self):
        # always sync, pip-df sync is relatively fast
        return False

    def sync_dependencies(self):
        with self.safe_activation():
            self.platform.check_command(self._pip_df_sync_cmd())
