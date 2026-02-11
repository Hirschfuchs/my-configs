from base import SubModule


class Hilfsprogramme(SubModule):
    def __init__(self):
        super().__init__(
            "hilfsprogramme",
            native_packages=[
                # Video- und Medienplayer (Open Source & sehr flexibel)
                "vlc",
                # VIM für Notizen im Terminal
                "vim",
                # Bildverarbeitung
                "imagemagick"
                # Versionsverwaltung
                "git",
                # Terminal
                "kitty",
                # Editor (ersetzt Sublime)
                "zed",
                # Dateiverschlüsselungstool
                "age",
                # Dateiverschlüsselungseditor
                "sops",
            ],
        )
