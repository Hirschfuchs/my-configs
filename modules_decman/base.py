import decman


class SubModule(decman.Module):
    def __init__(
        self,
        name,
        native_packages=None,
        aur_packages=None,
        flatpak_packages=None,
        submodules=None,
    ):
        super().__init__(name)

        self.native_packages = native_packages or []
        self.aur_packages = aur_packages or []
        self.flatpak_packages = flatpak_packages or []
        self.submodules = submodules or []

        decman.modules += [self]

    # Führt Pakete von Submodulen rekursiv zusammen
    def collect_packages(self):
        native = list(self.native_packages)
        foreign = list(self.aur_packages)
        flatpak = list(self.flatpak_packages)

        for module in self.submodules:
            sub_native, sub_foreign, sub_flatpak = module.collect_packages()
            native.extend(sub_native)
            foreign.extend(sub_foreign)
            flatpak.extend(sub_flatpak)

        return native, foreign, flatpak
