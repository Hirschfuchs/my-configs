from .base import SubModule


class Hilfsprogramme(SubModule):
    def __init__(self):
        super().__init__(
            "hilfsprogramme",
            native_packages=[
                # Video- und Medienplayer (Open Source & sehr flexibel) mit Codecs
                "vlc",
                "vlc-plugin-ffmpeg",
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
                # Komprimierung (RAR)
                "rar",
                # Autoklicker
                # "xautoclick",
            ],
            flatpak_packages=[
                # GUI für Git (ersetzt gitg)
                # Fehlende PGP-Signaturen bei Installation der Abgängigkeit garden-tools
                "com.github.git_cola.git-cola"
            ],
            desktop_links=[
                (
                    "dev.zed.Zed.desktop",
                    0,
                    1160
                ),
                (
                    "kitty.desktop",
                    0,
                    1150,
                    True
                ),
                (
                    "hilfsprogramme",
                    0,
                    115
                ),
            ],
            folder_links=[
                (
                    "hilfsprogramme",
                    "Hilfsprogramme",
                    [
                        (
                            "vlc.desktop",
                            12
                        ),
                        (
                            "com.github.git_cola.git-cola.desktop",
                            10
                        ),
                        (
                            "org.kde.kdiff3.desktop",
                            8
                        ),
                        (
                            "vim.desktop",
                            6
                        ),
                    ]
                ),
            ],
        )
