from ..base import SubModule


class XOrg(SubModule):
    def __init__(self):
        super().__init__(
            "X.org",
            native_packages=[
                # Xorg Display Server
                "xorg-server",
                # Xorg Direkteinstieg
                "xorg-init"
            ]
        )
