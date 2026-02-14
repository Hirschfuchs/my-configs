from .base import SubModule


class Spotify(SubModule):
    def __init__(self):
        super().__init__(
            "spotify",
            native_packages=[
                # Client
                "spotify-launcher",
            ],
            aur_packages=[
                # CLI-Steuerung für Spotify-Client
                # "spotify-tui",
                # Skins für Spotify
                "spicetify-cli",
                # Marktplatz für Spicetify-Plugins
                "spicetify-marketplace-bin",
            ]
        )
