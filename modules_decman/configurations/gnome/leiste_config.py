from modules_decman.configurations.base import SystemConfiguration


class LeisteConfig(SystemConfiguration):
    def __init__(self, username):
        super().__init__(
            name="Desktopleisten-Einstellungen",
            gsettings=[
                # Datum in Uhr anzeigen
                (
                    username,
                    "org.gnome.desktop.interface",
                    "clock-show-date",
                    "true"
                ),
                # Sekunden in Uhr anzeigen
                (
                    username,
                    "org.gnome.desktop.interface",
                    "clock-show-seconds",
                    "true"
                ),
                # Wochentag in Uhr anzeigen
                (
                    username,
                    "org.gnome.desktop.interface",
                    "clock-show-weekday",
                    "true"
                ),
                # Anzeige der Wochennummer im Schnellzugriffs-Kalender
                (
                    username,
                    "org.gnome.desktop.calendar",
                    "show-weekdate",
                    "true"
                ),
                # Anzeige des Ladestands in Prozent neben dem Ladestandsymbol
                (
                    username,
                    "org.gnome.desktop.interface",
                    "show-battery-percentage",
                    "true"
                ),
                # Die Option "Abmelden" soll auch angezeigt werden, wenn nur ein User existiert
                (
                    username,
                    "org.gnome.shell",
                    "always-show-log-out",
                    "false"
                ),
            ]
        )