from mlProject import logging
from pathlib import Path
import urllib.request
import os,zipfile
from mlProject.config.configuration import *


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
        
    def download_file(self):
        if not os.path.exists(self.config.local_data_path):
            urllib.request.urlretrieve(self.config.URL,self.config.local_data_path)
            logging.info('Zip data Doenloaded')
            
        else:
            logging.info('file Already exists')
            
    def Extract_Zip(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_path,'r') as file:
            file.extractall(unzip_path)
            logging.info('File Extract successfully')    