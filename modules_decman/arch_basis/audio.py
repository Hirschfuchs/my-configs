from ..base import SubModule


class Audio(SubModule):
    def __init__(self):
        super().__init__(
            "audio",
            native_packages=[
                # TODO: OSS ist veraltet, es muss vollständig auf Pulse umgestellt werden

                # ALSA Zentraler Audiotreiber
                "alsa-firmware",
                # Steuerung für ALSA
                "alsa-utils",

                # ALSA Libraries
                "alsa-lib",
                "lib32-alsa-lib",

                # ASLA-Pipewire-Brücke
                "pipewire-alsa",

                # ALSA-OSS-Brücke
                "alsa-oss",
            ],
            aur_packages=[
                # Alter Open Sound System Treiber
                "oss",
            ]
        )
