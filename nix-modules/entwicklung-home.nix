{ config, pkgs, lib, nixGL, ... }:
let
  pkgList = (import ./entwicklung-packages.nix { inherit pkgs; });
in {
  home.packages = lib.concatLists [ pkgList ];
  # TODO: Allow Unfree für jetbrains-toolbox

  xdg.desktopEntries.arduino = {
    type = "Application";
    name = "Arduino IDE";
    comment = "Proprietäre IDE für die Arduino-Entwicklung";
    exec = "${pkgs.arduino-ide}/bin/arduino";
    terminal = false;
    categories = [ "Development" "IDE" ];
  };
}