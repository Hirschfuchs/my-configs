from ..base import SubModule


class DruckerBrother(SubModule):
    def __init__(self):
        super().__init__(
            "brother mfc-j5730dw",
            aur_packages=[
                # Drucker Treiber
                "brother-mfc-j5730dw"
            ]
        )
