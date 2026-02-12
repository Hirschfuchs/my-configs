from ..base import SubModule


class Razer(SubModule):
    def __init__(self):
        super().__init__(
            "razer",
            native_packages=[
                # Freier Treiber und Verwaltungswerkzeug
                "openrazer-daemon",
            ]
        )
