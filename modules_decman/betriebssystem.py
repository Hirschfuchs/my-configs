from base import SubModule
from modules_decman.arch_basis.arch_basisdienste import ArchBasisdienste
from modules_decman.arch_basis.arch_minimum import ArchMinimum
from modules_decman.arch_basis.audio import Audio
from modules_decman.arch_basis.bluetooth import Bluetooth
from modules_decman.arch_basis.xorg import XOrg


class Betriebssystem(SubModule):
    def __init__(self):
        super().__init__(
            "betriebssystem",
            submodules=[
                ArchMinimum(),
                ArchBasisdienste(),
                Bluetooth(),
                Audio(),
                XOrg(),
            ],
            aur_packages=[
                # Decman muss sich selbst kennen
                "decman",
            ]
        )
