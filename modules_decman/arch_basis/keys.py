from ..base import SubModule


class Keys(SubModule):
    def __init__(self):
        super().__init__(
            "keys",
            native_packages=[
                # Automatisches Ziehen der aktuellen Mirrors
                "reflector",
                # Auffrischen des Keyrings
                "archlinux-keyring",
            ]
        )
