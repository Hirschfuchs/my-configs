import decman


class SubModule(decman.Module):
    def __init__(self, name, native_packages=None, aur_packages=None):
        super().__init__(name)

        self.native_packages = native_packages or []
        self.aur_packages = aur_packages or []
