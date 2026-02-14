import decman
import os


# --- AUTOMATISCHER BUILD-FIX ---
# Bei der Installation größerer Mengen Pakete aus dem AUR
# können Fehler durch nicht ausreichenden RAM-Speicher auftreten.
# Daher werden die Pakete auf der Festplatte gespeichert
BUILD_PATH = "/tmp/decman"
PERSISTENT_PATH = "/var/lib/decman-build"


class AurFix(decman.Module):
    def __init__(self) -> None:
        super().__init__("aur-fix")

    def before_update (self, store):
        print("Vorbereiten der persistierten Buildumgebung")

        if not os.path.exists (PERSISTENT_PATH):
            decman.prg(
                ["sudo", "mkdir", "-p", PERSISTENT_PATH],
            )
            decman.prg(
                ["sudo", "chmod", "777", PERSISTENT_PATH],
            )
        if os.path.ismount(BUILD_PATH):
            decman.prg(
                ["sudo", "umount", "-l", BUILD_PATH],
            )
        if os.path.exists(BUILD_PATH):
            decman.prg(
                ["sudo", "rm", "-rf", BUILD_PATH],
            )

        os.symlink(PERSISTENT_PATH, BUILD_PATH)
        print(f"Symlink erstellt von {BUILD_PATH} auf {PERSISTENT_PATH}")

    def after_update (self, store):
        print("Aufräumen der Buildumgebung")
        if os.path.islink(BUILD_PATH):
            os.remove(BUILD_PATH)
        if os.path.exists (PERSISTENT_PATH):
            decman.prg(
                ["sudo", "rm", "-rf", PERSISTENT_PATH],
            )
