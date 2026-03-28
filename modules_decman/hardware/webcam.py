from ..base import SubModule


class Webcam(SubModule):
    def __init__(self):
        super().__init__(
            "webcam-programme",
            aur_packages=[
                # OBSBOT Tiny Steuerung (GUI)
                "tiny4linux-gui",
                # OBSBOT Tiny Steuerung (CLI)
                "tiny4linux-cli",
                # V4L2 GUI
                "camset",
            ]
        )
