import decman


class SubModule(decman.Module):
    def __init__(
        self,
        name,
        native_packages=None,
        aur_packages=None,
        submodules=None,
    ):
        super().__init__(name)

        self.native_packages = native_packages or []
        self.aur_packages = aur_packages or []
        self.submodules = submodules or []

    # Führt Pakete von Submodulen rekursiv zusammen
    def collect_packages(self):
        native = list(self.native_packages)
        foreign = list(self.aur_packages)

        for module in self.submodules:
            sub_native, sub_foreign = module.collect_packages()
            native.extend(sub_native)
            foreign.extend(sub_foreign)

        return native, foreign
