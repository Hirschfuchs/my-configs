{ lib }: {
  smartPackages = { config, pkgs, packages }: let
    isNixOS = lib.hasAttr "environment" config;
  in
    if isNixOS then { environment.systemPackages = packages; }
    else { home.packages = packages; };
}
