from mlProject.config.configuration import *
from mlProject import logging
import pandas as pd 
import os
from sklearn.model_selection import 


class DataTransfomation:
    def __init__(self,config:DataTransfomationConfig) -> None:
        self.config=config
        
    def split_data(self):
        data=pd.read_csv(self.config.data_path)
        
        train_data,test_data=    