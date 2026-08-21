from .a11y import A11y
from .base import SubModule
from modules_decman.programmieren.datenbanken import Datenbanken
from modules_decman.programmieren.programmiersprachen import Programmiersprachen
from modules_decman.programmieren.sonstiges import EntwicklungSonstiges


class Entwicklung(SubModule):
    def __init__(self, username):
        super().__init__(
            "entwicklung",
            native_packages=[
                # SSH Client
                "putty",
                # FTP Client
                "filezilla",
                # Farbwähler
                "eyedropper",
                # Automatisierte Codedokumentation
                "doxygen",
                # Imaging Tool für Raspberry Pis (benötigt zum Flashen der CCU)
                "rpi-imager"
            ],
            aur_packages=[
                # Jetbrains Tools (IntelliJ, Webstorm & co.)
                "jetbrains-toolbox",
                # Arduino IDE
                "arduino-ide-bin",
                # HTTP Client
                "postman-bin",
            ],
            submodules=[
                Programmiersprachen(),
                Datenbanken(),
                EntwicklungSonstiges(),
                A11y(username),
            ],
            desktop_links=[
                (
                    "jetbrains-ides",
                    0,
                    850,
                ),
                (
                    "dev-clients",
                    0,
                    848,
                ),
                (
                    "dev-support",
                    0,
                    846,
                ),
            ],
            folder_links=[
                (
                    "jetbrains-ides",
                    "Jetbrains IDEs",
                    [
                        (
                            "jetbrains-toolbox.desktop",
                            2,
                        ),
                        (
                            "jetbrains-webstorm-ae46fdbf-5479-4483-8828-9331e5ef124c.desktop",
                            12,
                        ),
                        (
                            "jetbrains-idea-ce-ad70273b-2cef-430b-b4cc-394f9432e75d.desktop",
                            11,
                        ),
                        (
                            "jetbrains-pycharm-a02f3784-b348-4164-aad5-e44dedd24c0f.desktop",
                            10,
                        ),
                        (
                            "jetbrains-rustrover-0c05fa69-c2ca-4831-a530-d2b09e7cad3a.desktop",
                            8,
                        ),
                        (
                            "jetbrains-rubymine-43214cba-25f8-46f4-90ce-f3326bfd220d.desktop",
                            7,
                        ),
                        (
                            "jetbrains-studio-26e583bd-5b3f-49ec-a09e-47e584cb4e11.desktop",
                            6,
                        ),
                    ],
                ),
                (
                    "dev-clients",
                    "Entwicklungs-Clients",
                    [
                        (
                            "filezilla.desktop",
                            10
                        ),
                        (
                            "putty.desktop",
                            9
                        ),
                        (
                            "postman.desktop",
                            8
                        ),
                    ]
                ),
                (
                    "dev-support",
                    "Entwicklungsunterstützung",
                    [
                        (
                            "com.github.finefindus.eyedropper.desktop",
                            14
                        ),
                        (
                            "com.raspberrypi.rpi-imager.desktop",
                            3
                        ),
                    ]
                ),
            ],
        )
