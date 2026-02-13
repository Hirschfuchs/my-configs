from base import SubModule


class Virtualisierung(SubModule):
    def __init__(self):
        super().__init__(
            "virtualisierung",
            native_packages=[
                # Linux Containers (OS-Level Virtualisierung)
                "lxc",
                # Virtual Box (ISO-VMs)
                "virtualbox",
                # Zugriff auf mehr Hardware- und OS-Schichten für volle VM-Nutzbarkeit
                "virtualbox-guest-iso",
            ]
        )
