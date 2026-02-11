from base import SubModule


class Standardprogramme(SubModule):
    def __init__(self):
        super().__init__(
            "standardprogramme",
            native_packages=[
                # Browser
                "firefox",
                # Passwortmanager
                "keepass",
                # Taschenrechner
                "qalculate-qt"
            ]
        )
