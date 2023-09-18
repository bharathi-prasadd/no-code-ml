{ nixpkgs ? import <nixpkgs> {} }:

with nixpkgs;

let
  pythonPackages = python310Packages;  # Adjust to your Python version if needed

in
stdenv.mkDerivation {
  name = "no-code-ml";

  buildInputs = [
    pythonPackages.torchvision# Add any other dependencies as needed
    pythonPackages.torch # Add any other dependencies as needed
  ];

  shellHook = ''
    export PYTHONPATH=$PYTHONPATH:${pythonPackages.torchvision}/lib/python3.8/site-packages
  '';
}
