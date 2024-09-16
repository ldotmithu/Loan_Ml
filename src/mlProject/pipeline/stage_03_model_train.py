from mlProject.components.model_training import*
from mlProject import logging
from mlProject.config.configuration import *


class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        config=ConfigurationManager()
        model_training_config=config.get_model_train_config()
        model_training=ModelTraining(config=model_training_config)
        model_training.preprocess_method()
        model_training.train_model()
