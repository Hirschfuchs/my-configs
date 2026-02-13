from base import SubModule


class A11y(SubModule):
    def __init__(self):
        super().__init__(
            "barrierefreiheit",
            native_packages=[
                # GNOME-Screenreader
                "orca",
            ]
        )
