from ..base import SubModule


class Behringer(SubModule):
    def __init__(self):
        super().__init__(
            "behringer-programme",
            aur_packages=[
                # GUI für Behringer X-Air
                "xairedit-bin",
            ],
            desktop_links=[
                (
                    "xairedit.desktop",
                    1,
                    400,
                    True,
                ),
            ],
        )
