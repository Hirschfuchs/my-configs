import decman
from ..base import SubModule
from ..configurations.base import SystemConfiguration

class Netzwerk(SubModule):
    def __init__(self):
        super().__init__(
            "netzwerk",
            native_packages=[
                # CLI für WLAN-Konfiguration
                "iw",
                # Wireless Daemon
                "iwd",
                # Paketverfolgung
                "traceroute",
            ],
            configurations = [
                SystemConfiguration(
                    name="Erweiterte Netzwerkkonfiguration",
                    systemd_units=["iwd.service"],
                )
            ],
        )
