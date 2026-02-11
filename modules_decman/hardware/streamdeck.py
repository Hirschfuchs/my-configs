from ..base import SubModule


class Streamdeck(SubModule):
    def __init__(self):
        super().__init__(
            "streamdeck-programme",
            aur_packages=[
                # Streamdeck Steuerung (GUI)
                "streamcontroller"
            ]
        )
