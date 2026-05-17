from src.ML_Project.logger import logger
from src.ML_Project.exception import CustomException
from src.ML_Project.Components.data_ingestion import DataIngestion

if __name__ == "__main__":

    logger.info("Running: app.py")
    try:
        data_ingestion = DataIngestion()
        train_path, test_path = data_ingestion.setup()

    except Exception as e:
        raise CustomException(e)