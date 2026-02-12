from base import SubModule


class Standardprogramme(SubModule):
    def __init__(self):
        super().__init__(
            "standardprogramme",
            native_packages=[
                # Passwortmanager
                "keepass",
                # Taschenrechner
                "qalculate-qt",
                # Partitionsmanager
                "partitionmanager",
            ],
            aur_packages=[
                # Browser
                "google-chrome",
            ]
        )
