import os
import sys
import pandas as pd
from dataclasses import dataclass
from src.ML_Project.logger import logger
from src.ML_Project.exception import CustomException
from dotenv import load_dotenv
import pymysql


logger.info("Env Setup in utils")
load_dotenv()
host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
db = os.getenv('db')

def read_data():
    logger.info("Reading Data from database in utils")
    try:
        database = pymysql.connect(
            host = host,
            user = user,
            password= password,
            db = db
        )
        logger.info("Connected to : ", database)

        data = pd.read_sql_query('Select * from table_name', database)

        return data

    except Exception as e:
        raise CustomException(e)
