import shutil
import decman
from pathlib import Path


REPO_PATH = Path("./assets/desktop")
BACKGROUND_PROPERTIES_PATH = Path("/usr/share/gnome-background-properties")
BACKGROUNDS_PATH = Path("/usr/share/backgrounds/fox")

VERSION_FILE_NAME = "dynamic-background.version"
PROPERTIES_FILE_NAME = "dynamic.xml"

LOCAL_VERSION_FILE = REPO_PATH / VERSION_FILE_NAME
CURRENT_VERSION_FILE = BACKGROUND_PROPERTIES_PATH / VERSION_FILE_NAME

LOCAL_PROPERTIES_FILE = REPO_PATH / PROPERTIES_FILE_NAME
CURRENT_PROPERTIES_FILE = BACKGROUND_PROPERTIES_PATH / PROPERTIES_FILE_NAME

class BackgroundChanger(decman.Module):
    def __init__(self) -> None:
        super().__init__("background-changer")

    def after_update (self, store):
        print("Prüfen des Desktophintergrunds auf Aktualität")

        if not LOCAL_VERSION_FILE.exists():
            print(f"Lokale Repo-Versionsdatei {LOCAL_VERSION_FILE} nicht gefunden!")
            return

        local_version = LOCAL_VERSION_FILE.read_text().strip()

        system_version = None
        if CURRENT_VERSION_FILE.exists():
            system_version = CURRENT_VERSION_FILE.read_text().strip()

        if system_version == local_version:
            print("Der Desktophintergrund ist aktuell. Es sind keine Änderungen notwendig.")
            return

        print("Der Desktophintergrund wird aktualisiert.")

        if system_version != None:
            print("Vorherige Version: " + system_version)

        print("Neue Version: " + local_version)

        try:
            BACKGROUND_PROPERTIES_PATH.mkdir(parents=True, exist_ok=True)
            BACKGROUNDS_PATH.mkdir(parents=True, exist_ok=True)

            # TODO: Dynamische Dateinamen und -endungen ermöglichen
            files_to_move = ["background-bright.jpg", "background-dark.jpg", "sources.md"]
            for filename in files_to_move:
                src = REPO_PATH / filename
                dst = BACKGROUNDS_PATH / filename

                if src.exists():
                    shutil.copy2(str(src), str(dst))
                else:
                    print(f"Warnung: Die Quelldatei {src} wurde nicht gefunden.")

            if LOCAL_PROPERTIES_FILE.exists():
                shutil.copy2(str(LOCAL_PROPERTIES_FILE), str(CURRENT_PROPERTIES_FILE))
                print("Desktop-Hintergrund-Konfiguration wurde aktualisiert.")
            else:
                print(f"Warnung: Die Konfigurationsdatei {LOCAL_PROPERTIES_FILE} wurde nicht gefunden.")

            shutil.copy2(str(LOCAL_VERSION_FILE), str(CURRENT_VERSION_FILE))

        except PermissionError:
            print("Fehler: Das Skript hat nicht die notwendigen Schreibrechte zum aktualisieren der Hintergründe!")
        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")
