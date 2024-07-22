from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv("SQL_URL_STRING")

#Connection string for MySQL Workbench
SQLALCHEMY_DATABASE_URL= database_url

#In my case, I needed to use the "MySQL-Connector" string to connect to my database in MySQL Workbench

#https://docs.sqlalchemy.org/en/20/dialects/mysql.html#module-sqlalchemy.dialects.mysql.mysqlconnector

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()