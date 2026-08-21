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
                # Bildbetrachter
                "nomacs",
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
            ],
            desktop_links=[
                (
                    "firefox.desktop",
                    0,
                    1190
                ),
                (
                    "google-chrome.desktop",
                    0,
                    1189
                ),
                (
                    "keepass.desktop",
                    0,
                    1180
                ),
                (
                    "io.github.Qalculate.qalculate-qt.desktop",
                    0,
                    410
                ),
                (
                    "pdf4qt",
                    0,
                    90
                ),
                (
                    "de.bund.ausweisapp.ausweisapp2.desktop",
                    0,
                    64
                ),
            ],
            folder_links=[
                (
                    "pdf4qt",
                    "PDF Programme",
                    [
                        (
                            "io.github.JakubMelka.Pdf4qt.desktop",
                            10
                        ),
                        (
                            "io.github.JakubMelka.Pdf4qt.Pdf4QtEditor.desktop",
                            8
                        ),
                        (
                            "io.github.JakubMelka.Pdf4qt.Pdf4QtViewer.desktop",
                            7
                        ),
                        (
                            "io.github.JakubMelka.Pdf4qt.Pdf4QtDiff.desktop",
                            6
                        ),
                        (
                            "io.github.JakubMelka.Pdf4qt.Pdf4QtPageMaster.desktop",
                            4
                        ),
                    ],
                ),
            ],
        )
