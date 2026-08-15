import decman
import os
import decman.config
from decman.extras.users import User, UserManager

from modules_decman.configurations.aur_fix import AurFix


class HostBase(decman.Module):
    def __init__(self, name, submodules, subkonfigurationen=None):
        super().__init__(name)

        decman.modules += [AurFix()]

        subkonfigurationen = subkonfigurationen or []
        submodules = submodules or []

        # Pakete
        native = []
        foreign = []
        flatpak = []
        modulkonfigurationen = []

        # Konfigurationen
        angewendete_konfigurationen = []
        systemd_units = []
        commands = []
        gsettings = []
        config_files = []
        config_dirs = []

        for module in submodules:
            sub_native, sub_foreign, sub_flatpak, sub_configurations = module.collect_packages()
            native.extend(sub_native)
            foreign.extend(sub_foreign)
            flatpak.extend(sub_flatpak)
            modulkonfigurationen.extend(sub_configurations)

        # Direkt übergebene Konfigurationen
        for konfiguration in subkonfigurationen:
            config_namen, sub_systemd_units, sub_commands, sub_gsettings, sub_config_files, sub_config_dirs = konfiguration.collect_configs()
            angewendete_konfigurationen.extend(config_namen)
            systemd_units.extend(sub_systemd_units)
            commands.extend(sub_commands)
            gsettings.extend(sub_gsettings)
            config_files.extend(sub_config_files)
            config_dirs.extend(sub_config_dirs)

        # Über Module definierte Konfigurationen
        for konfiguration in modulkonfigurationen:
            config_namen, sub_systemd_units, sub_commands, sub_gsettings, sub_config_files, sub_config_dirs = konfiguration.collect_configs()
            angewendete_konfigurationen.extend(config_namen)
            systemd_units.extend(sub_systemd_units)
            commands.extend(sub_commands)
            gsettings.extend(sub_gsettings)
            config_files.extend(sub_config_files)
            config_dirs.extend(sub_config_dirs)

        # Duplikate entfernen
        native = sorted(set(native))
        foreign = sorted(set(foreign))
        flatpak = sorted(set(flatpak))
        systemd_units = sorted(set(systemd_units))

        decman.config.cache_dir = "/var/cache/decman"

        decman.pacman.packages |= set(native)
        decman.aur.packages |= set(foreign)
        decman.flatpak.packages |= set(flatpak)

        # Aktivieren der in den Konfigurationen definierten SystemD-Units
        if getattr(decman.systemd, "enabled_units", None) is None:
            decman.systemd.enabled_units = systemd_units
        else:
            decman.systemd.enabled_units.update(systemd_units)

        # Hinzufügen der in den Konfigurationen definierten Dateien und Verzeichnisse
        for config_directory in set(config_dirs):
            decman.modules.append(
                decman.files.Directory(
                    name=f"dir_{config_directory.strip('/').replace('/', '_')}",
                    path=config_directory
                )
            )
        for file_tuple in set(config_files):
            path = file_tuple[0]
            content = file_tuple[1]

            # Default-Werte setzen, falls das Tupel kürzer ist
            mode = file_tuple[2] if len(file_tuple) > 2 else "0644"
            owner = file_tuple[3] if len(file_tuple) > 3 else "root"
            group = file_tuple[4] if len(file_tuple) > 4 else "root"

            decman.modules.append(
                decman.files.File(
                    name=f"file_{path.strip('/').replace('/', '_')}",
                    path=path,
                    content=content,
                    mode=mode,
                    owner=owner,
                    group=group
                )
            )

        # Speichern der Kommandos für nach den Installationen
        self.angewendete_konfigurationen = sorted(set(angewendete_konfigurationen))
        self.gsettings = gsettings
        self.commands = commands

        decman.execution_order = [
            "files",
            "pacman",
            "aur",
            "flatpak",
            "systemd"
        ]

        um = UserManager()
        um.add_user(User(
            username="builduser",
            home="/var/lib/builduser",
            system=True,
        ))

        os.environ["GNUPGHOME"] = "/var/lib/builduser/gnupg"
        decman.aur.makepkg_user = "builduser"

        decman.modules += [um]

    def after_update (self, store):
        # Anzeige aller angewendeten Konfigurationen
        konfigurations_namen = self.angewendete_konfigurationen

        if konfigurations_namen:
            formatted_names = "\\n - ".join(konfigurations_namen)
            print_cmd = f"echo -e '\\n========================================\\n[Decman] Folgende Konfigurationen werden angewendet:\\n - {formatted_names}\\n========================================\\n'"

            decman.sh(print_cmd)

        commands = self.commands

        # Anwenden der konfigurierten GSettings
        for user, schema, key, value in self.gsettings:
            # 1. Ermitteln der UID des Ziel-Users für den DBUS-Socket (Standard bei Systemd: /run/user/<UID>)
            # 2. Ausführen als Ziel-User mit direkter Anbindung an seinen DBUS-Socket
            cmd = (
                f"sudo -u {user} "
                f"DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/$(id -u {user})/bus "
                f"gsettings set {schema} {key} \"{value}\""
            )
            commands.append(cmd)

        # Anwenden der konfigurierten Kommandos
        for command in sorted(set(commands)):
            decman.sh(command)
