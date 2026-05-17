import os
import pandas as pd
from dataclasses import dataclass
from src.ML_Project.logger import logger
from src.ML_Project.exception import CustomException
from src.ML_Project.utils import read_data
from sklearn.model_selection import train_test_split
@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join("Data", 'train.csv')
    test_data_path:str = os.path.join("Data", 'test.csv')
    raw_data_path:str = os.path.join("Data", 'raw.csv')


class DataIngestion:
    def __init__(self):
        self.config = DataIngestionConfig()

    def setup(self):
        try:
            os.makedirs(os.path.dirname(self.config.raw_data_path), exist_ok=True)
            logger.info("Reading Data from database")

            # loading raw data from database and save into folder 
            raw = read_data()
            raw.to_csv(self.config.raw_data_path, index=False, header=True)
            logger.info("Saved raw Data from database")


            # train test split and save in path 
            train, test = train_test_split(raw, test_size=0.2, random_state=42)

            train.to_csv(self.config.train_data_path, index=False, header=True)
            test.to_csv(self.config.test_data_path, index=False, header=True)
            logger.info("Saved train and test data")

            return (self.config.train_data_path, self.config.test_data_path)

        except Exception as e:
            raise CustomException(e)