from ..base import SubModule


class Controller(SubModule):
    def __init__(self):
        super().__init__(
            "controller",
            native_packages=[
                # Mapper für Gamepads & Joysticks
                "antimicrox",
            ],
        )
