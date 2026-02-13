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
            ]
        )
