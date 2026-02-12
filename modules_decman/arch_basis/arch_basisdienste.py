from ..base import SubModule


class ArchBasisdienste(SubModule):
    def __init__(self):
        super().__init__(
            "arch-basisdienste",
            native_packages=[
                # Daemon für ACPI-Ereignisse (behandelt z. B. Power-Button, Laptop-Deckel)
                "acpid",
                # Nachrichtenbus-System zur Kommunikation zwischen Prozessen (IPC)
                "dbus",
                # Zero-Conf-Networking (mDNS/DNS-SD) zur automatischen Geräte- und Dienstsuche
                "avahi",
                # Drucksystem
                "cups",
            ]
        )
