from base import SubModule


class Individualisierung(SubModule):
    def __init__(self):
        super().__init__(
            "individualisierung",
            aur_packages=[
                # Anpassung für Grub-Bootmenü
                "grub-customizer",
            ]
        )
