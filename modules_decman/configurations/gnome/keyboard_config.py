from modules_decman.configurations.base import SystemConfiguration


class KeyboardConfig(SystemConfiguration):
    def __init__(self, username):
        super().__init__(
            "Tastaturkonfiguration",
            gsettings=[
                # Ich verwende ein deutsches Tastaturlayout ohne Dead Keys
                (
                    username,
                    "org.gnome.desktop.input-sources",
                    "sources",
                    "[('xkb', 'de+nodeadkeys')]"
                ),
                # Compose-Taste
                (
                    username,
                    "org.gnome.desktop.input-sources",
                    "xkb-options",
                    "['compose:rctrl']"
                ),
            ]
        )
