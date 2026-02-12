from ...base import SubModule


class Horizon(SubModule):
    def __init__(self):
        super().__init__(
            "horizon-client",
            native_packages=[
                # Client
                "vmware-horizon-client",
                # Benötigte Keymaps
                "vmware-keymaps",
            ]
        )
