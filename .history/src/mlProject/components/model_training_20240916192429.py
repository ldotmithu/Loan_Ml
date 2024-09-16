from mlProject.config.configuration import *
from mlProject import logging
import pandas as pd 


class ModelTraining:
    def __init__(self,config:ModelTrainingConfig) -> None:
        self.config=config
        
    def preprocess_method(self):
        train_data=pd.read_csv(self.config.train_data_path)
        test_data=pd.read_csv(self.config.test_data_path)
        
           