from ..base import SubModule
import decman


class Streamdeck(SubModule):
    def __init__(self):
        super().__init__(
            "streamdeck-programme",
            flatpak_packages=[
                # Streamdeck Steuerung (GUI)
                # AUR-Installation wirft aktuell Fehler scikit_build_core._vendor.pyproject_metadata.errors.ConfigurationError
                "com.core447.StreamController",
            ]
        )

    def after_update (self, store):
        print("Ermögliche StreamController Gnome-Shell-Zugriff")
        decman.prg(
            ["flatpak", "override", "--user", "--talk-name=org.gnome.Shell.Extensions.Windows", "com.core447.StreamController"],
        )