from .base import SubModule
from modules_decman.hardware.behringer import Behringer
from modules_decman.hardware.drucker_brother import DruckerBrother
from modules_decman.hardware.hardware_monitoring import HardwareMonitoring
from modules_decman.hardware.ptouch_print import PTouchPrint
from modules_decman.hardware.razer import Razer
from modules_decman.hardware.rgb_beleuchtung import RgbBeleuchtung
from modules_decman.hardware.streamdeck import Streamdeck
from modules_decman.hardware.webcam import Webcam


class HardwareCoburg(SubModule):
    def __init__(self):
        super().__init__(
            "hardware-coburg",
            submodules=[
                Razer(),
                Behringer(),
                Webcam(),
                Streamdeck(),
                DruckerBrother(),
                HardwareMonitoring(),
                RgbBeleuchtung(),
                PTouchPrint(),
            ]
        )
