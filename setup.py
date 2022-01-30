import os
from distutils.dir_util import copy_tree
from distutils.file_util import copy_file

src_dir = "web-toolbox/"

links = [
    ".eslintrc.js",
    ".pre-commit-config.yaml", 
    ".prettierrc", 
    "package.json", 
    "rollup.config.dev.js", 
    "rollup.config.prod.js",
    "tsconfig.json"
]

init_copies = [
    "src/",
    ".gitignore"
]

force_copies = [
    "src/copy/favicon.png"
]

for link in links:
    src = src_dir+link
    dest = link
    print("Linking", src, "to", dest)
    os.remove(dest)
    os.symlink(src, dest)

for copy in init_copies:
    src = src_dir+copy
    dest = copy

    if os.path.isfile(dest) or os.path.isdir(dest):
        print("dest", dest, "already exists. Skipping...")
        continue

    print("Copying", src, "to", dest)
    if os.path.isdir(src):
        copied = copy_tree(src, dest)
        print("Files copied:", copied)
    elif os.path.isfile(src):
        copy_file(src, dest)
    else:
        print("ERROR - can't find source file/dir to copy:", src)

for copy in force_copies:
    src = src_dir+copy
    dest = copy
    print("Copying", src, "to", dest)
    copy_file(src, dest)
