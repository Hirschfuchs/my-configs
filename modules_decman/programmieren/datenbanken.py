from ..base import SubModule


class Datenbanken(SubModule):
    def __init__(self):
        super().__init__(
            "datenbanken-clis",
            native_packages=[
                "aws-cli-v2",
                "influx-cli",
                "mariadb",
                "mysql-workbench",
                "postgresql",
            ]
        )
