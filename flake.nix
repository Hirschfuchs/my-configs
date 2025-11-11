{
    description = "Multi-host nix configuration";

    inputs = {
        nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.05";
        home-manager.url = "github:nix-community/home-manager";
        home-manager.inputs.nixpkgs.follows = "nixpkgs";
    };

    nixConfig = {
        experimental-features = [ "nix-command" "flakes" ];
    };

    outputs = { self, nixpkgs, home-manager, flake-utils, ... }:
    {
        # Konfigurationen für Nicht-NixOS-Linux-Systeme
        homeConfigurations = {
            techtornado-arch = home-manager.lib.homeManagerConfiguration {
                pkgs = import nixpkgs { system = "x86_64-linux"; };

                modules = [
                    ./hosts/techtornado-arch.nix
                ];
            };
        };
    };
}