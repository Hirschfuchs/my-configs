from ..base import SubModule


class ArchMinimum(SubModule):
    def __init__(self):
        super().__init__(
            "arch-minimum",
            native_packages=[
                # Linux Standard-Kernel (Alternativen: linux-lts, linux-hardened)
                "linux",
                # Firmwareunterstützung Kernel
                "linux-firmware",
                # Metapaket für Minimalsystem
                "base",
                # Ermöglichen von Paketbau
                "base-devel",
                # Netzwerkverbindung ermöglichen
                "networkmanager",
            ]
        )
