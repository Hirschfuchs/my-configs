from sys import stdout

import decman


class HostBase(decman.Module):
    def __init__(self, name, submodules):
        super().__init__(name)

        native = []
        foreign = []

        for module in submodules:
            sub_native, sub_foreign = module.collect_packages()
            native.extend(sub_native)
            foreign.extend(sub_foreign)

        # Duplikate entfernen
        native = sorted(set(native))
        foreign = sorted(set(foreign))

        decman.pacman.packages |= set(native)
        decman.aur.packages |= set(foreign)
