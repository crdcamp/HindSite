import os
from pathlib import Path

BASE_DIR = Path(os.path.abspath(os.path.dirname(__file__))).parent

DATA_DIR = BASE_DIR / "data"

for directory in []:
    directory.mkdir(parents=True, exist_ok=True)