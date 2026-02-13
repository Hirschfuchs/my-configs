from ..base import SubModule


class RgbBeleuchtung(SubModule):
    def __init__(self):
        super().__init__(
            "beleuchtungssteuerung",
            native_packages=[
                # Markenübergreifende LED-Steuerung
                "openrgb",
            ],
            aur_packages=[
                # Nutzung von Hue Entertainment auf Linux
                "huestacean",
            ]
        )
