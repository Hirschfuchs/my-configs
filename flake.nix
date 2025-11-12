{
    description = "Multi-host nix configuration";

    inputs = {
        nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.05";
        home-manager.url = "github:nix-community/home-manager/release-25.05";
        home-manager.inputs.nixpkgs.follows = "nixpkgs";

        nixGL = {
            url = "github:nix-community/nixGL";
            inputs.nixpkgs.follows = "nixpkgs";
        };
    };

    nixConfig = {
        experimental-features = [ "nix-command" "flakes" ];
    };

    outputs = { self, nixpkgs, home-manager, nixGL, ... }: {
      homeConfigurations = {
        techtornado-arch = home-manager.lib.homeManagerConfiguration {
          pkgs = import nixpkgs {
            system = "x86_64-linux";
            # TODO: Unfree für Nvidia erlauben
          };

          extraSpecialArgs = {
            inherit nixGL;
          };

          modules = [
            ./hosts/techtornado-arch.nix
          ];
        };
      };
    };
}