from sys import stdout

import decman
import decman.config

from modules_decman.configurations.aur_fix import AurFix


class HostBase(decman.Module):
    def __init__(self, name, submodules):
        super().__init__(name)

        decman.modules += [AurFix()]

        native = []
        foreign = []
        flatpak = []

        for module in submodules:
            sub_native, sub_foreign, sub_flatpak = module.collect_packages()
            native.extend(sub_native)
            foreign.extend(sub_foreign)
            flatpak.extend(sub_flatpak)

        # Duplikate entfernen
        native = sorted(set(native))
        foreign = sorted(set(foreign))
        flatpak = sorted(set(flatpak))

        decman.config.cache_dir = "/var/cache/decman"

        decman.pacman.packages |= set(native)
        decman.aur.packages |= set(foreign)
        decman.flatpak.packages |= set(flatpak)

        decman.execution_order = [
            "files",
            "pacman",
            "aur",
            "flatpak",
            "systemd",
        ]
