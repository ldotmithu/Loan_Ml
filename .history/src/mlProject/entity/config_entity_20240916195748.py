from pathlib import Path
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    root_dir: Path
    URL: str
    local_data_path: Path
    unzip_dir: Path
    
@dataclass
class DataTransfomationConfig:
    root_dir: Path
    data_path:Path  
    
@dataclass
class ModelTrainingConfig:
    root_dir:Path
    train_data_path: Path
    test_data_path: Path
    model_name:str
    preprocess_file:str      