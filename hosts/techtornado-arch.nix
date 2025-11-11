{ config, pkgs, lib, ... }:
{
    home.username = "bono";
    home.homeDirectory = "/home/bono";

    imports = [
        ../nix-modules/hilfsprogramme.nix
    ];

    programs.zsh.enable = true;
    programs.zsh.shell = pkgs.zsh;
    home.stateVersion = "25.05";
}