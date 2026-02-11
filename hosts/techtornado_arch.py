from base import HostBase

from modules_decman.hilfsprogramme import Hilfsprogramme
from modules_decman.standardprogramme import Standardprogramme
from modules_decman.entwicklung import Entwicklung
from modules_decman.kommunikation_privat import KommunikationPrivat


class TechtornadoArch(HostBase):
    def __init__(self):
        super().__init__(
            "techtornado-arch",
            submodules=[
                Hilfsprogramme(),
                Standardprogramme(),
                Entwicklung(),
                KommunikationPrivat()
            ],
        )
