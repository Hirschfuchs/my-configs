from .base import SubModule


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
                "imagemagick",
                # Dokumentenverwaltung
                "pandoc-cli",
                # Versionsverwaltung
                "git",
                # Unterstützung großer Dateien in Git
                "git-lfs",
                # Terminal
                "kitty",
                # Editor (ersetzt Sublime)
                "zed",
                # Dateiverschlüsselungstool
                "age",
                # Dateiverschlüsselungseditor
                "sops",
                # Komprimierung
                "zip",
                # App für Batch-Umbenennungen
                "krename",
                # Dateivergleich
                "kdiff3",
                # "Als PDF drucken" für CUPS Druckservice
                "cups-pdf",
                # Erkennung von Packages, die neu gebaut werden müssen
                "rebuild-detector",
                # Darstellung von Systeminformationen
                "fastfetch",
                # Autovervollständigung in der Bash
                "bash-completion",
            ],
            aur_packages=[
                # GUI für Git (ersetzt gitg)
                "git-cola",
                # Komprimierung (RAR)
                "rar",
                # Autoklicker
                "xautoclick",
            ]
        )
