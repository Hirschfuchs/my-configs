from .base import SubModule


class MedienVerarbeitung(SubModule):
    def __init__(self):
        super().__init__(
            "medien-verarbeitung",
            native_packages=[
                # DVD-Tools
                "libdvdread",
                "libdvdnav",
                "libdvdcss",
                # Video-Transcoder
                "handbrake",
                # YouTube Downloader
                "yt-dlp",
                # Bild-zu-PDF-Konvertierer
                "img2pdf",
            ],
            aur_packages=[
                # BluRay Wiedergabe
                "makemkv",
                "makemkv-libaacs",
            ],
            folder_links=[
                (
                    "hilfsprogramme",
                    "Hilfsprogramme",
                    [
                        (
                            "fr.handbrake.ghb.desktop",
                            9
                        ),
                    ]
                ),
            ],
        )
