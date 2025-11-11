{ config, pkgs, lib, ... }:

let
  smartModule = import ./modules.nix { inherit lib; };
in
smartModule.smartPackages { inherit config pkgs; packages = with pkgs; [
    vlc
    vim
    sublime
    kitty
    imagemagick
    git
]; }
