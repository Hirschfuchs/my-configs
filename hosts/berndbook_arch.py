from modules_decman.configurations.base import SystemConfiguration
from .base import HostBase
from modules_decman.a11y import A11y
from modules_decman.bildbearbeitung import Bildbearbeitung
from modules_decman.arch_basis.firmware_treiber.cpu_intel import CpuIntel
from modules_decman.betriebssystem import Betriebssystem
from modules_decman.desktop import Desktop
from modules_decman.fun import Fun

from modules_decman.hilfsprogramme import Hilfsprogramme
from modules_decman.individualisierung import Individualisierung
from modules_decman.medien_verarbeitung import MedienVerarbeitung
from modules_decman.spotify import Spotify
from modules_decman.standardprogramme import Standardprogramme
from modules_decman.entwicklung import Entwicklung
from modules_decman.kommunikation_privat import KommunikationPrivat
from modules_decman.textverarbeitung import Textverarbeitung


class BerndBookArch(HostBase):
    def __init__(self):
        self.username = "Bono"

        super().__init__(
            "bernd-das-book-arch",
            username=self.username,
            submodules=[
                Betriebssystem(),
                Desktop(self.username),
                Hilfsprogramme(),
                Standardprogramme(),
                Textverarbeitung(),
                MedienVerarbeitung(),
                Entwicklung(self.username),
                KommunikationPrivat(),
                CpuIntel(),
                Individualisierung(),
                Bildbearbeitung(),
                Spotify(),
                A11y(self.username),
                Fun(),
            ],
            subkonfigurationen=[
                SystemConfiguration(
                    name="Bernd das Book System-Konfiguration",
                    commands=[
                        (
                            f"echo -e '\\n========================================\\n"
                            f"[Decman] Entferne Standard-Netzwerk-Supplicant\\n"
                            f"========================================\\n'"
                        ),
                        "sudo systemctl disable wpa_supplicant --now",
                    ]
                )
            ]
        )
