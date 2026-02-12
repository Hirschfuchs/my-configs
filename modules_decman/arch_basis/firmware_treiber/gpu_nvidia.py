from ...base import SubModule


class GpuNvidia(SubModule):
    def __init__(self):
        super().__init__(
            "firmware-gpu-nvidia",
            native_packages=[
                # Quelloffener NVIDIA Treiber
                "nvidia-open",
            ]
        )
