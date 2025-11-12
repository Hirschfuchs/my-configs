{ config, pkgs, lib, nixGL, ... }:
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

    nixGL = {
        packages = nixGL.packages;
        defaultWrapper = "mesa";
        offloadWrapper = "nvidiaPrime";
        installScripts = [ "mesa" "nvidiaPrime" ];
      };

    home.sessionVariables = {
      NIX_CONFIG = "experimental-features = nix-command flakes";
    };

    home.sessionPath = [ "${config.home.homeDirectory}/.nix-profile/bin" ];

    home.stateVersion = "25.05";
}