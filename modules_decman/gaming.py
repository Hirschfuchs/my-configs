from .base import SubModule
from modules_decman.hardware.controller import Controller
from modules_decman.hardware.lenkrad import Lenkrad


class Gaming(SubModule):
    def __init__(self):
        super().__init__(
            "kommunikation-weitere",
            native_packages=[
                # Steam Client
                # multilib muss unter /etc/pacman.conf aktiviert werden
                # TODO: automatisieren
                "steam",
                # Winetricks-Adaption für Steam-/Proton-Apps
                "protontricks",
            ],
            aur_packages=[
                # Cutechess Schach
                "cutechess",
                # Stockfish Schach Engine
                "stockfish-git",
                # Berserk UCI compliant Schach Engine
                "berserk",
                # KATEGORIE Minecraft
                # Management & Starter für Modded & Vanilla Minecraft
                "multimc-bin",
                # Technic Launcher
                "minecraft-technic-launcher",
                # Echtwelt-Map-Generator für beliebige Orte
                "arnis-bin",
                #
                # Starten von Java-Webanwendungen (StellwerkSim)
                "openwebstart-bin",
            ],
            flatpak_packages=[
                # Vollwertige gekapselte Windows-Umgebung
                "com.usebottles.bottles"
            ],
            submodules=[
                Lenkrad(),
                Controller(),
            ],
            desktop_links=[
                (
                    "steam.desktop",
                    0,
                    1000
                ),
                (
                    "multimc.desktop",
                    0,
                    900
                ),
                (
                    "minecrafttools",
                    1,
                    120
                ),
            ],
            folder_links=[
                (
                    "minecrafttools",
                    "Minecraft-Tools",
                    [
                        (
                            "technic-launcher.desktop",
                            10
                        ),
                        (
                            "arnis.desktop",
                            9
                        ),
                    ]
                )
            ]
        )
