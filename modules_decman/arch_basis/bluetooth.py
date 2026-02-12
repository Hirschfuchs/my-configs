from ..base import SubModule


class Bluetooth(SubModule):
    def __init__(self):
        super().__init__(
            "bluetooth",
            native_packages=[
                # Bluetooth-Protokollstack
                "bluez-utils",
            ]
        )
