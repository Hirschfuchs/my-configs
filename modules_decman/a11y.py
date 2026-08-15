from .base import SubModule
from .configurations.base import SystemConfiguration


class A11y(SubModule):
    def __init__(self, username):
        super().__init__(
            "barrierefreiheit",
            native_packages=[
                # GNOME-Screenreader
                "orca",
            ],
            configurations=[
                SystemConfiguration(
                    name="Barrierefreiheit",
                    gsettings=[
                        # Barrierefreiheitssymbol dauerhaft anzeigen
                        (
                            username,
                            "org.gnome.desktop.a11y",
                            "always-show-universal-access-status",
                            "true"
                        )
                    ]
                )
            ]
        )
