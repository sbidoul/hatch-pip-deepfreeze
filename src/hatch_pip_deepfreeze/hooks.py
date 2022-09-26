# SPDX-FileCopyrightText: 2022-present Stéphane Bidoul <stephane.bidoul@acsone.eu>
#
# SPDX-License-Identifier: MIT

from hatchling.plugin import hookimpl

from .plugin import PipDeepfreezeEnvironment


@hookimpl
def hatch_register_environment():
    return PipDeepfreezeEnvironment
