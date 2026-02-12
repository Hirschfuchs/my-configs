from base import SubModule
from modules_decman.programmieren.datenbanken import Datenbanken
from modules_decman.programmieren.programmiersprachen import Programmiersprachen


class Entwicklung(SubModule):
    def __init__(self):
        super().__init__(
            "entwicklung",
            native_packages=[
                # SSH Client
                "putty",
                # FTP Client
                "filezilla",
                # Farbwähler
                "eyedropper"
            ],
            aur_packages=[
                # Jetbrains Tools (IntelliJ, Webstorm & co.)
                "jetbrains-toolbox",
                # Arduino IDE
                "arduino-ide-bin",
                # HTTP Client
                "postman-bin"
            ],
            submodules=[
                Programmiersprachen(),
                Datenbanken(),
            ]
        )
