from pathlib import Path
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    root_dir: Path
    URL: str
    local_data_path: Path
    unzip_dir: Path