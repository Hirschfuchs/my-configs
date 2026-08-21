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
            ],
            desktop_links=[
                (
                    "libre_suite",
                    0,
                    800
                ),
            ],
            folder_links=[
                (
                    "libre_suite",
                    "LibreOffice Suite",
                    [
                        (
                            "libreoffice-startcenter.desktop",
                            2
                        ),
                        (
                            "libreoffice-writer.desktop",
                            18
                        ),
                        (
                            "libreoffice-calc.desktop",
                            17
                        ),
                        (
                            "libreoffice-impress.desktop",
                            16
                        ),
                        (
                            "libreoffice-base.desktop",
                            5
                        ),
                        (
                            "libreoffice-draw.desktop",
                            5
                        ),
                        (
                            "libreoffice-math.desktop",
                            5
                        ),
                    ]
                )
            ]
        )
