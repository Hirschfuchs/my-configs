from ..base import SubModule


class EntwicklungSonstiges(SubModule):
    def __init__(self):
        super().__init__(
            "entwicklung-sonstiges",
            native_packages=[
                "github-cli",
            ]
        )
