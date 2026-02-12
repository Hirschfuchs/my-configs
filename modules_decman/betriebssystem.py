from base import SubModule
from modules_decman.arch_basis.arch_basisdienste import ArchBasisdienste
from modules_decman.arch_basis.arch_minimum import ArchMinimum
from modules_decman.arch_basis.bluetooth import Bluetooth


class Betriebssystem(SubModule):
    def __init__(self):
        super().__init__(
            "betriebssystem",
            submodules=[
                ArchMinimum(),
                ArchBasisdienste(),
                Bluetooth(),
            ]
        )
