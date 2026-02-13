from base import SubModule
from modules_decman.backup import Backup


class Standardprogramme(SubModule):
    def __init__(self):
        super().__init__(
            "standardprogramme",
            native_packages=[
                # Passwortmanager
                "keepass",
                # Taschenrechner
                "qalculate-qt",
                # Partitionsmanager
                "partitionmanager",
            ],
            aur_packages=[
                # Browser
                "google-chrome",
                # elektronischer Ausweis
                "ausweisapp2",
                # Bildbetrachter (ersetzt Gwenview)
                "qimgv-git",
            ],
            submodules=[
                Backup()
            ]
        )
