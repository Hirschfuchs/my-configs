from .base import SubModule


class Textverarbeitung(SubModule):
    def __init__(self):
        super().__init__(
            "textverarbeitung",
            native_packages=[
                # Libreoffice (Fresh Version)
                "libreoffice-fresh",
                # Deutsche Sprachunterstützung für Libre Office
                "libreoffice-fresh-de",
            ]
        )
