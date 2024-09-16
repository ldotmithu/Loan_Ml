from mlProject import logging
from pathlib import Path
import urllib.request
import os
from mlProject.config.configuration import *


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
        
    def download_file(self):
        if not os.path.exists(self.config.local_data_path):
            urllib.request.urlretrieve(self.config.URL,self.config.local_data_path)
            logging.info('Zip data Doenloaded')
            
        else:
            logging.info('')        