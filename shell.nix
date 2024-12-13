let 
  pkgs = import <nixpkgs> {};
in
pkgs.mkShell {
  packages = [
    pkgs.zsh
    (pkgs.python3.withPackages (python-pkgs: with python-pkgs; [
      pip
      tkinter
    ]))
  ];
  shellHook = ''
    zsh
    echo "Welcome to my Deutsch Python project"
  '';
}
