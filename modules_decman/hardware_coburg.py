from base import SubModule
from modules_decman.hardware.streamdeck import Streamdeck
from modules_decman.hardware.webcam import Webcam


class HardwareCoburg(SubModule):
    def __init__(self):
        super().__init__(
            "hardware-coburg",
            submodules=[
                Webcam(),
                Streamdeck()
            ]
        )
