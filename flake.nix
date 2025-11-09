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
        flake-utils.lib.eachDefaultSystem (system:
            let pkgs = import nixpkgs { inherit system; };
            in {
                # Konfigurationen für Nicht-NixOS-Linux-Systeme
                homeConfigurations = {
                    techtornado-arch = home-manager.lib.homeConfiguration {
                        inherit pkgs;
                        configuration = import ./hosts/techtornado-arch.nix;
                    };
                };
            }
    );
}