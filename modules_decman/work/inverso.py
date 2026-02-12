from .modules.horizon import Horizon
from ..base import SubModule


class Inverso(SubModule):
    def __init__(self):
        super().__init__(
            "inverso",
            submodules=[
                Horizon(),
            ],
            aur_packages=[
                # Webex
                "webex-bin",
            ]
        )
