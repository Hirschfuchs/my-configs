from .base import SubModule


class Ventoy(SubModule):
    def __init__(self):
        super().__init__(
            "ventoy",
            native_packages=[
                # Generierung einer Arch-ISO
                "archiso",
            ],
            aur_packages=[
                # Ventoy Tools
                "ventoy",
            ],
        )
