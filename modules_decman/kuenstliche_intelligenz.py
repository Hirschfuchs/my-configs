from modules_decman.base import SubModule


class KuenstlicheIntelligenz(SubModule):
    def __init__(self):
        super().__init__(
            "Künstliche Intelligenzen",
            aur_packages=[
                # Runtime für lokale Ausführung von KIs
                "lmstudio-bin",
            ],
            desktop_links=[
                (
                    "lmstudio.desktop",
                    0,
                    765
                ),
            ],
        )