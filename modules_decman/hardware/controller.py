from ..base import SubModule


class Controller(SubModule):
    def __init__(self):
        super().__init__(
            "controller",
            native_packages=[
                # Mapper für Gamepads & Joysticks
                "antimicrox",
            ],
            aur_packages=[
                # Unterstützung für das Microsoft Game Input Protocol (XBox-Controller)
                "xone-dkms",
            ]
        )
