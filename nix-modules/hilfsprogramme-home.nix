{ config, pkgs, lib, nixGL, ... }:
let
  wrapWithNixGl = pkg: config.lib.nixGL.wrappers.nvidiaPrime pkg;
  pkgList = (import ./hilfsprogramme-packages.nix { inherit pkgs; });
  pkgListNixGlRaw = (import ./hilfsprogramme-packages-nixgl.nix { inherit pkgs; });
  pkgListNixGlWrapped = lib.map (pkg: config.lib.nixGL.wrapOffload pkg) pkgListNixGlRaw;
in {
  home.packages = lib.concatLists [ pkgList pkgListNixGlWrapped ];
}