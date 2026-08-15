from ..base import SubModule
from ..configurations.base import SystemConfiguration


class Keys(SubModule):
    def __init__(self):
        super().__init__(
            "keys",
            native_packages=[
                # Automatisches Ziehen der aktuellen Mirrors
                "reflector",
                # Auffrischen des Keyrings
                "archlinux-keyring",
            ],
            configurations=[
                SystemConfiguration(
                    name="Reflektoraktivierung",
                    systemd_units=["reflector.service"]
                )
            ]
        )
