from base import SubModule


class KommunikationWeitere(SubModule):
    def __init__(self):
        super().__init__(
            "kommunikation-weitere",
            native_packages=[
                # Signal
                "signal-desktop",
                # Team Speak
                "teamspeak3",
            ],
            aur_packages=[
                # Zoom
                "zoom",
            ]
        )
