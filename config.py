import os
from pathlib import Path

BASE_DIR = Path(os.path.abspath(os.path.dirname(__file__))).parent

DATA_DIR = BASE_DIR / "data" / "metadata"

for directory in [DATA_DIR]:
    directory.mkdir(parents=True, exist_ok=True)