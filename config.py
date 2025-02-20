import os
from pathlib import Path

BASE_DIR = Path(os.path.abspath(os.path.dirname(__file__))).parent

DATA_DIR = BASE_DIR / "data"
LEARNING_DIR = BASE_DIR / "learning resources"

for directory in [DATA_DIR, LEARNING_DIR]:
    directory.mkdir(parents=True, exist_ok=True)