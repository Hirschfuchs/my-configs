from .base import SubModule


class Fonts(SubModule):
    def __init__(self):
        super().__init__(
            "schriftarten",
            native_packages=[
                # Ubuntu Font Family
                "ttf-ubuntu-font-family",
                # Jetbrains Mono-Font
                "ttf-jetbrains-mono",
                # Noto Emoji
                "noto-fonts-emoji",
            ],
            aur_packages=[
                # Dyslexia Fonts
                # "open-dyslexic-fonts",
            ]
        )
