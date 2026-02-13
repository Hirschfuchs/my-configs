from .base import SubModule


class Fun(SubModule):
    def __init__(self):
        super().__init__(
            "fun-stuff",
            native_packages=[
                # Terminal-Aquarium
                "asciiquarium",
                # Kuh hat wichtige Ansagen zu machen
                "cowsay",
                # Digitaler Regen aus Matrix
                "cmatrix",
            ],
            aur_packages=[
                # Katze zum Jagen meiner Maus
                "oneko",
            ]
        )
