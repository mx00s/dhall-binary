#!/usr/bin/env python3

import os
import pathlib
import shutil

ROOT = pathlib.Path(__file__).parent.parent.resolve()

def write_dhall_file(dir, name, content):
    fname = f"{dir}/{name}.dhall"
    with open(fname, "w") as f:
        f.write(content)
    with open(f"{dir}/{name}", "w") as f:
        f.write(f"./{name}.dhall\n")

def handle_bit_width(b):
    n = 2 ** b
    
    prefix = "B"
    current = f"{prefix}{n}"
    previous = f"{prefix}{n >> 1}"

    dir = f"{ROOT}/{current}"
    shutil.rmtree(dir, ignore_errors=True)
    os.mkdir(dir)

    dhall_code = {
        "Type": f"{{ _1 : ../{previous}/Type, _2 : ../{previous}/Type }}\n",
        "toBitString":
f"""let toBitString
    : ./Type -> ../BitString/Type
    = \(b : ./Type) ->
        (../Prelude).List.concat
          ../B1/Type
          [ ../{previous}/toBitString b._1, ../{previous}/toBitString b._2 ]

in  toBitString
""",
        "render": "\(b : ./Type) -> ../BitString/render (./toBitString b)\n"
    }

    for name, content in dhall_code.items():
        write_dhall_file(dir, name, content)

if __name__ == "__main__":
    for b in range(1, 8):
        handle_bit_width(b)
