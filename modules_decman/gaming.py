from base import SubModule
from modules_decman.hardware.lenkrad import Lenkrad


class Gaming(SubModule):
    def __init__(self):
        super().__init__(
            "kommunikation-weitere",
            native_packages=[
                # Steam Client
                "steam",
                # Mapper für Gamepads & Joysticks
                "antimicrox",
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
            submodules=[
                Lenkrad(),
            ]
        )
