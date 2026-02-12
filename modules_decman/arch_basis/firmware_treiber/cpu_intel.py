from ...base import SubModule


class CpuIntel(SubModule):
    def __init__(self):
        super().__init__(
            "cpu_intel",
            native_packages=[
                # Ermöglicht Microcode-Zugriff für Intel-CPUs
                "intel-ucode",
            ]
        )
