from .base import SubModule
from modules_decman.backup import Backup
from modules_decman.fonts import Fonts


class Standardprogramme(SubModule):
    def __init__(self):
        super().__init__(
            "standardprogramme",
            native_packages=[
                # Browser
                "firefox",
                # Passwortmanager
                "keepass",
                # Taschenrechner
                "qalculate-qt",
                # Partitionsmanager
                "partitionmanager",
                # Flatpak Paketmanager
                "flatpak",
            ],
            aur_packages=[
                # Browser
                "google-chrome",
                # Bildbetrachter (ersetzt Gwenview)
                "qimgv-git",
                # PDF-Bearbeitung
                "pdf4qt",
            ],
            flatpak_packages=[
                # elektronischer Ausweis
                "de.bund.ausweisapp.ausweisapp2",
            ],
            submodules=[
                Backup(),
                Fonts()
            ]
        )
