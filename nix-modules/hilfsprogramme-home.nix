{ config, pkgs, lib, ... }:
let
  pkgList = (import ./hilfsprogramme-packages.nix { inherit pkgs; });
in {
  home.packages = lib.concatLists [ pkgList ];
}