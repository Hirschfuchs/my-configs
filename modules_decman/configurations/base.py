import decman


# Definierte Konfigurationen müssen stets idempotent sein,
# da sie bei jedem Systemupdate angewendet werden!
class SystemConfiguration(decman.Module):
    def __init__(
            self,
            name,
            systemd_units=None,
            commands=None,
            gsettings=None,
            config_files=None,
            config_dirs=None,
            subconfigs=None,
    ):
        super().__init__(name)

        self.systemd_units = systemd_units or []
        self.commands = commands or []
        self.gsettings = gsettings or []
        self.config_files = config_files or []
        self.config_dirs = config_dirs or []
        self.subconfigs = subconfigs or []

        decman.modules += [self]

    # Führt Konfigurationselemente von Subkonfigurationen rekursiv zusammen
    def collect_configs(self):
        systemd_units = list(self.systemd_units)
        commands = list(self.commands)
        gsettings = list(self.gsettings)
        config_files = list(self.config_files)
        config_dirs = list(self.config_dirs)

        for konfiguration in self.subconfigs:
            sub_systemd_units, sub_commands, sub_gsettings, sub_config_files, sub_config_dirs = konfiguration.collect_configs()
            systemd_units.extend(sub_systemd_units)
            commands.extend(sub_commands)
            gsettings.extend(sub_gsettings)
            config_files.extend(sub_config_files)
            config_dirs.extend(sub_config_dirs)

        return systemd_units, commands, gsettings, config_files, config_dirs
