from base import SubModule


class Bildschirmaufnahme(SubModule):
    def __init__(self):
        super().__init__(
            "bildschirmaufnahme",
            native_packages=[
                # OBS
                "obs-studio",
            ]
        )
