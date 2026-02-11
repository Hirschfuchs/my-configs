from base import HostBase

from modules_decman.hilfsprogramme import Hilfsprogramme


class TechtornadoArch(HostBase):
    def __init__(self):
        super().__init__(
            "techtornado-arch",
            submodules=[
                Hilfsprogramme(),
            ],
        )
