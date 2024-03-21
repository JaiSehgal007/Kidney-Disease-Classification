from KidneyDiseaseClassifier import logger
from KidneyDiseaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

# from src.KidneyDiseaseClassifier import logger
# we need not write like this as KidneyDiseaseClassifier is installed as a local package

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nX================================X")
except Exception as e:
    logger.exception(e)
    raise e