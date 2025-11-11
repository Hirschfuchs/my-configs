{ lib }: {
  smartPackages = { config, pkgs, packages }: let
    isHomeManager = lib.hasAttr "home" config;
  in
    if isHomeManager then { home.packages = packages; }
    else { environment.systemPackages = packages; };
}
