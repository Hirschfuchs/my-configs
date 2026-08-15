from modules_decman.configurations.base import SystemConfiguration


class MultitaskingConfig(SystemConfiguration):
    def __init__(self, username):
        super().__init__(
            name="Multitasking Konfiguration",
            gsettings=[
                # Das Berühren der oberen linken Ecke soll nicht die Aktivitäten-Übersicht öffnen
                (
                    username,
                    "org.gnome.desktop.interface",
                    "enable-hot-corners",
                    "false"
                ),
                # Das Ziehen von Fenstern an Bildschirmränder soll deren Größe anpassen
                (
                    username,
                    "org.gnome.mutter",
                    "edge-tiling",
                    "true"
                ),
                # Die Anzahl der Arbeitsflächen soll dynamisch sein
                (
                    username,
                    "org.gnome.mutter",
                    "dynamic-workspaces",
                    "true"
                ),
                # Nur der Hauptbildschirm soll wechselbare Arbeitsflächen haben
                (
                    username,
                    "org.gnome.mutter",
                    "workspaces-only-on-primary",
                    "true"
                ),
                # Buttonreihenfolge für Fenster
                (
                    username,
                    "org.gnome.desktop.wm.preferences",
                    "button-layout",
                    "'appmenu:minimize,maximize,close'"
                )
            ]
        )
