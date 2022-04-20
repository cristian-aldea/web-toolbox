import os
import shutil
from ast import List
from unittest import case

src_dir = "web-toolbox/"

sources = [
    "assets/",
    "public/",
    "src/",
    ".eslintrc.js",
    ".pre-commit-config.yaml",
    ".prettierrc",
    "index.html",
    "vite.config.js"
]

for source in sources:
    src = src_dir+source
    dest = source

    if not os.path.exists(src):
        print("ERROR - Failed to find source "+src+". Skipping")
        continue

    print("\nProcessing '"+src+"' -> '"+dest+"' ", end="")


    if os.path.isfile(src):
        shutil.copy(src, dest)
    else:
        shutil.copytree(src, dest, dirs_exist_ok=True)
