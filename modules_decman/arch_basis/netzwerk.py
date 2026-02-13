from ..base import SubModule


class Netzwerk(SubModule):
    def __init__(self):
        super().__init__(
            "netzwerk",
            native_packages=[
                # CLI für WLAN-Konfiguration
                "iw",
                # Wireless Daemon
                "iwd",
            ]
        )
