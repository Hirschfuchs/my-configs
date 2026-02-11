from base import HostBase

from modules_decman.hilfsprogramme import Hilfsprogramme
from modules_decman.entwicklung import Entwicklung


class TechtornadoArch(HostBase):
    def __init__(self):
        super().__init__(
            "techtornado-arch",
            submodules=[
                Hilfsprogramme(),
                Entwicklung(),
            ],
        )
