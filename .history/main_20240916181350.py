from mlProject.pipeline.stage_01_data_ingestion import *
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