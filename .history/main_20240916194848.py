from mlProject.pipeline.stage_01_data_ingestion import *
from mlProject.pipeline.stage_02_data_transfomation import *
from mlProject.pipeline.stage_03_model_train import *
from mlProject import logging

Stage_Name='Data Ingestion Satge'
try:
    data_ingestion=DataIngestionPipeline()
    data_ingestion.main()
    logging.info('Data Ingestion Completed')
    logging.info('>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('                                         ')
except Exception as e:
    logging.exception(e)
    raise e 



Stage_Name='Data Transfomation Satge'
try:
    data_transfomation=DataTransfomationPipeline()
    data_transfomation.main()
    logging.info('Data Transfomation Completed')
    logging.info('>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('                                         ')
except Exception as e:
    logging.exception(e)
    raise e

Stage_Name='Model Train Satge'
try:
    model_training=ModelTrainingPipeline()
    model_training.main()
    logging.info('Data Transfomation Completed')
    logging.info('>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print('                                         ')
except Exception as e:
    logging.exception(e)
    raise e