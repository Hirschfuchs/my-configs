# Meine Konfigurationen
Dieses Repo enthält die Konfigurationen für meine Geräte.

Enthalten sollen verschiedene NixOS- bzw. Nix-Konfigurationsdateien für Linux,
sowie Chocolatey-Listen für Windowssysteme.

Weiterhin wird der Aufbau in Asciidoc dokumentiert und Entscheidungen begründet,
sodass zu einem späteren Zeitpunkt der Aufbau leicht nachvollzogen werden kann.

## Generierung der Dokumentation
Die Dokumentation des Projektes erfolgt in Asciidoc.
Zur Generierung der Doku in PDF-Form wird Ruby mit einigen Gems benötigt.
Die erforderlichen Gems sind bereits hinterlegt und können via `bundle install`
installiert werden.
Ggf. ist `bundle config set --local path 'vendor/bundle'` dafür nötig.
