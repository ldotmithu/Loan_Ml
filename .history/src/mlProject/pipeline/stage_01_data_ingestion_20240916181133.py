from mlProject.components.data_ingestion import *
from mlProject.config.configuration import *
from mlProject.entity.config_entity import *


class DataIngestionPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.Extract_Zip()