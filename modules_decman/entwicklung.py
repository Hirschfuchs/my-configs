from base import SubModule


class Entwicklung(SubModule):
    def __init__(self):
        super().__init__(
            "entwicklung",
            aur_packages=[
                # Jetbrains Tools (IntelliJ, Webstorm & co.)
                "jetbrains-toolbox",
                # Arduino IDE
                "arduino-ide-bin"
            ],
        )
