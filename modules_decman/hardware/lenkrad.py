from ..base import SubModule


class Lenkrad(SubModule):
    def __init__(self):
        super().__init__(
            "lenkräder",
            aur_packages=[
                # Systemweite Verwaltung von Lenkrädern & Force Feedback
                "oversteer",
                # Kernel für Thrustmaster Lenkräder
                # "hid-tmff2-dkms-git",
                # PIDFF Treiber mit Fixes für Force Feedback
                "universal-pidff-dkms-git",
            ],
            flatpak_packages=[
                # Steuerung von MOZA Lenkrädern
                # AUR-Installation wirft Fehler bei Abhängigkeit python-trayer-git
                # Failed to build package 'python-trayer-git', because the pkg file cannot be determined. Possible files are: []
                "io.github.lawstorant.boxflat",
            ]
        )
