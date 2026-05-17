import os
import sys
import pandas as pd
from dotenv import load_dotenv
import pymysql


load_dotenv()
host = os.getenv('host')
user = os.getenv('user')
password = os.getenv('password')
db = os.getenv('db')

database = pymysql.connect(
            host = host,
            user = user,
            password= password,
            db = db
        )

data = pd.read_sql_query('Select * from fish', database)
print(data.head())