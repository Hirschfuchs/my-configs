from .base import SubModule


class Backup(SubModule):
    def __init__(self):
        super().__init__(
            "backup",
            native_packages=[
                # Backend für Backups
                "borg"
                # Frontend für Borg Backup
                "vorta",
            ]
        )
