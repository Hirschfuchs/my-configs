from base import SubModule


class Musizieren(SubModule):
    def __init__(self):
        super().__init__(
            "musizieren (DAWs und co)",
            aur_packages=[
                # Synthesia-Alternative zum Keyboard-Üben
                "neothesia",
            ]
        )
