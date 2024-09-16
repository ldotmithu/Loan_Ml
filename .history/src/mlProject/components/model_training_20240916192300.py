from mlProject.config.configuration import *
from mlProject import logging


class ModelTraining:
    def __init__(self,config:ModelTrainingConfig) -> None:
        self.config=config