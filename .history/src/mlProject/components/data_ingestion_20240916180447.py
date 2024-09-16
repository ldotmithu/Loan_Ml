from mlProject import logging
from pathlib import Path
import urllib.request
import os
from mlProject.config.configuration import *


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
        
    def download_file(self):
            