{ config, pkgs, lib, ... }:
{
    home.username = "bono";
    home.homeDirectory = "/home/bono";

    imports = [
        ../nix-modules/hilfsprogramme-home.nix
    ];

    programs.zsh = {
      enable = true;
      package = pkgs.zsh;
    };

    home.stateVersion = "25.05";
}