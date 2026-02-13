from ..base import SubModule


class PTouchPrint(SubModule):
    def __init__(self):
        super().__init__(
            "brother p-touch print",
            aur_packages=[
                # CLI-Tool zur Ansteuerung
                "ptouch-print",
            ]
        )
