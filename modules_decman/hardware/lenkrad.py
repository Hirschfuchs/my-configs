from ..base import SubModule


class Lenkrad(SubModule):
    def __init__(self):
        super().__init__(
            "lenkräder",
            aur_packages=[
                # Systemweite Verwaltung von Lenkrädern & Force Feedback
                "oversteer",
                # Steuerung von MOZA Lenkrädern
                # "boxflat-git",
                # Kernel für Thrustmaster Lenkräder
                # "hid-tmff2-dkms-git",
                # PIDFF Treiber mit Fixes für Force Feedback
                "universal-pidff-dkms-git",
            ]
        )
