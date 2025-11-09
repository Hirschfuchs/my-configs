{ config, pkgs, lib, ... }:
lib.smartPackages { inherit config pkgs; packages = with pkgs; [
    vlc
    vim
    sublime
    kitty
    imagemagick
    git
]; }
