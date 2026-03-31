import decman
from .base import SubModule
from .configurations.desktop_background import BackgroundChanger


class Desktop(SubModule):
    def __init__(self):
        super().__init__(
            "desktop (gnome)",
            native_packages=[
                # Display Manager (Login-Bildschirm)
                "gdm",
                # Gnome-Desktop-Shell
                "gnome-shell",
                # Verwaltung von Nutzer-Sessions
                "gnome-session",
                # Session-weite Nutzereinstellungen
                "gnome-settings-daemon",
                # Integration von xdg-user-dirs in GNOME/GTK
                "xdg-user-dirs-gtk",
                # Credentialsteuerung für Gnome
                "gnome-keyring",
                # GNOME-Dateimanager
                "nautilus",
                # Previewer für Nautilus
                "sushi",
                # Erweitertes Konfigurations-Tool für GNOME
                "gnome-tweaks",
                # Ermöglicht die Installation von Shell-Erweiterungen
                "gnome-shell-extensions",
                # Zentrales Kontrollzentrum für Systemeinstellungen
                "gnome-control-center",
                # Virtuelles Dateisystem (nötig für Handy-Anbindung/Netzwerk-Mounts)
                "gvfs",
                # KATEGORIE gvfs-Backends (siehe https://de.wikipedia.org/wiki/Gnome_Virtual_File_System)
                # SMB-Protokoll
                "gvfs-smb",
                #
                # Portals für GNOME (nötig für Sandboxed Apps / Flatpak)
                "xdg-desktop-portal-gnome",
                # Verwaltung von GNOME Umgebungen
                "dconf",
                "dconf-editor",
                # Menüstrukturen
                "gnome-menus",
                # Hintergrund-Management
                "gnome-backgrounds",
                # Farbprofil-Management
                "gnome-color-manager",
                # Festplattenbelegung
                "baobab",
                # Laufwerksverwaltung
                "gnome-disk-utility",
                # Tool für Datenaustausch
                "gnome-user-share",
                # E-Mail-Client
                "evolution",
                # Lautstärkeregler
                "pavucontrol",
                # Snapshot-Funktionalität
                "snapshot",
                # Hilfe-Betrachter für GNOME-Dokumentation (nötig für die Hilfe-Funktion vieler Apps)
                "yelp",
                # Tastaturlayout-Betrachter
                "tecla",
                # Task Manager
                "gnome-system-monitor",
                # Standard-Terminal
                "gnome-console",
            ],
            aur_packages= [
                # Automatischer Night-Mode
                "gnome-shell-extension-nightthemeswitcher",
            ]
        )

        decman.modules += [BackgroundChanger()]
