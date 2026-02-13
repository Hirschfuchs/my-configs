from base import HostBase
from modules_decman.a11y import A11y
from modules_decman.bildbearbeitung import Bildbearbeitung
from modules_decman.arch_basis.firmware_treiber.cpu_intel import CpuIntel
from modules_decman.arch_basis.firmware_treiber.gpu_nvidia import GpuNvidia
from modules_decman.betriebssystem import Betriebssystem
from modules_decman.desktop import Desktop
from modules_decman.fun import Fun
from modules_decman.gaming import Gaming

from modules_decman.hilfsprogramme import Hilfsprogramme
from modules_decman.kommunikation_weitere import KommunikationWeitere
from modules_decman.legacy import Legacy
from modules_decman.medien_verarbeitung import MedienVerarbeitung
from modules_decman.spotify import Spotify
from modules_decman.standardprogramme import Standardprogramme
from modules_decman.entwicklung import Entwicklung
from modules_decman.kommunikation_privat import KommunikationPrivat
from modules_decman.hardware_coburg import HardwareCoburg
from modules_decman.textverarbeitung import Textverarbeitung


class TechtornadoArch(HostBase):
    def __init__(self):
        super().__init__(
            "techtornado-arch",
            submodules=[
                Betriebssystem(),
                Desktop(),
                Hilfsprogramme(),
                Standardprogramme(),
                Textverarbeitung(),
                MedienVerarbeitung(),
                Entwicklung(),
                KommunikationPrivat(),
                KommunikationWeitere(),
                HardwareCoburg(),
                CpuIntel(),
                GpuNvidia(),
                Gaming(),
                Bildbearbeitung(),
                Spotify(),
                A11y(),
                Fun(),
                Legacy(),
            ],
        )
