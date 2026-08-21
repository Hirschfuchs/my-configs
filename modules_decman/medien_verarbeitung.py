from .base import SubModule


class MedienVerarbeitung(SubModule):
    def __init__(self):
        super().__init__(
            "medien-verarbeitung",
            native_packages=[
                # Video-Transcoder
                "handbrake",
                # YouTube Downloader
                "yt-dlp",
                # Bild-zu-PDF-Konvertierer
                "img2pdf",
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
