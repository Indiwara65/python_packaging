import os
from pathlib import Path

list_of_files = [
    "src/__init__.py",
    "src/module1/__init__.py",
    "src/module2/__init__.py",
    "test/integration",
    "test/unit",
    "reqirments.txt",
    "requirments_dev.txt",
    "pyproject.toml",
    ".gitignore",
    "tox.ini"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    dir, filename = os.path.split(filepath)
    print(f"dir:{dir}\nfilename:{filename}\n")