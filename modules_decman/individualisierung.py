from .base import SubModule


class Individualisierung(SubModule):
    def __init__(self):
        super().__init__(
            "individualisierung",
            aur_packages=[
                # Anpassung für Grub-Bootmenü
                "grub-customizer",
            ],
            folder_links=[
                (
                    "hilfsprogramme",
                    "Hilfsprogramme",
                    [
                        (
                            "grub-customizer.desktop",
                            3
                        ),
                    ]
                ),
            ]
        )
