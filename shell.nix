# shell.nix

let
    pkgs = import <nixpkgs> { overlays = [ ]; };
in pkgs.mkShell {
    packages = [
        (pkgs.python3.withPackages (py: [
            py.google-api-python-client
            py.google-auth-oauthlib
            py.google-auth-httplib2
            py.isodate
        ]))
        pkgs.curl
        pkgs.jq
    ];
}
