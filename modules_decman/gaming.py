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
                # Standard-Launcher (optional)
                "minecraft-launcher",
                # Technic Launcher (optional)
                "minecraft-technic-launcher",
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
            ]
        )
