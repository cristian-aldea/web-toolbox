import os
import shutil
from ast import List
from unittest import case

src_dir = "web-toolbox/"

sources = [
    "src/",
    "src/copy/favicon.png",
    ".eslintrc.js",
    ".gitignore",
    ".pre-commit-config.yaml",
    ".prettierrc",
    "package.json",
    "rollup.config.dev.js",
    "rollup.config.prod.js",
    "tsconfig.json"
]


def get_input(message: str, options: list[str]) -> int:
    while True:
        response = input(message)

        if response not in options:
            print("ERROR - please pick a value in", options)
            continue

        return response


for source in sources:
    src = src_dir+source
    dest = source

    if not os.path.exists(src):
        print("ERROR - Failed to find source "+src+". Skipping")
        continue

    print("\nProcessing '"+src+"' -> '"+dest+"' ", end="")

    if os.path.isdir(src):
        option = get_input(
            "PICK ONE: copy (c), skip (s): ", ["c", "s"])
    else:
        option = get_input(
            "PICK ONE: link (l), copy (c), skip (s): ", ["l", "c", "s"])

    if option != "s":
        if os.path.isfile(dest):
            os.remove(dest)
        elif os.path.isdir(dest):
            shutil.rmtree(dest)

    if option == "l":
        os.symlink(src, dest)
    elif option == "c":
        if os.path.isfile(src):
            shutil.copyfile(src, dest)
        else:
            shutil.copytree(src, dest)
    else:
        print("Skipping...")
