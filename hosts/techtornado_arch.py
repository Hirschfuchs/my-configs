from base import HostBase
from modules_decman.arch_basis.firmware_treiber.cpu_intel import CpuIntel
from modules_decman.arch_basis.firmware_treiber.gpu_nvidia import GpuNvidia
from modules_decman.betriebssystem import Betriebssystem

from modules_decman.hilfsprogramme import Hilfsprogramme
from modules_decman.standardprogramme import Standardprogramme
from modules_decman.entwicklung import Entwicklung
from modules_decman.kommunikation_privat import KommunikationPrivat
from modules_decman.hardware_coburg import HardwareCoburg


class TechtornadoArch(HostBase):
    def __init__(self):
        super().__init__(
            "techtornado-arch",
            submodules=[
                Betriebssystem(),
                Hilfsprogramme(),
                Standardprogramme(),
                Entwicklung(),
                KommunikationPrivat(),
                HardwareCoburg(),
                CpuIntel(),
                GpuNvidia(),
            ],
        )
