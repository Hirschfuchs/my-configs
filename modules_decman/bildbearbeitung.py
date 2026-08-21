from .base import SubModule


class Bildbearbeitung(SubModule):
    def __init__(self):
        super().__init__(
            "bildbearbeitung",
            native_packages=[
                # Lightroom-Alternative
                "rawtherapee",
                # Grafikprogramm
                "gimp",
                # Zeichenprogramm mit weiteren Bildbearbeitungsfunktionen
                "krita",
            ],
            desktop_links=[
                (
                    "bildverarbeitung",
                    0,
                    124
                )
            ],
            folder_links=[
                (
                    "bildverarbeitung",
                    "Bildverarbeitung",
                    [
                        (
                            "rawtherapee.desktop",
                            7
                        ),
                        (
                            "gimp.desktop",
                            5
                        ),
                        (
                            "org.kde.krita.desktop",
                            4
                        )
                    ]
                )
            ]
        )
