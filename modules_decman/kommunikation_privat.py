from base import SubModule


class KommunikationPrivat(SubModule):
    def __init__(self):
        super().__init__(
            "kommunikation-privat",
            native_packages=[
                # Discord
                "discord"
            ]
        )
