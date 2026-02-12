from ..base import SubModule


class HardwareMonitoring(SubModule):
    def __init__(self):
        super().__init__(
            "hardware-monitoring",
            native_packages=[
                # Überhitzungsschutz
                "thermald",
                # SSD Schutz (S.M.A.R.T)
                "smartmontools"
            ]
        )
