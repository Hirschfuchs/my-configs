import decman
from decman.plugins import pacman, aur


class HostBase(decman.Module):
    def __init__(self, name, submodules):
        super().__init__(name)

        native = []
        foreign = []

        for module in submodules:
            native.extend(module.native_packages)
            foreign.extend(module.aur_packages)

        # Duplikate entfernen
        native = sorted(set(native))
        foreign = sorted(set(foreign))

        pacman.packages(native)
        aur.packages(foreign)
