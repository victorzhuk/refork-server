from os import getenv
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

load_dotenv(find_dotenv())

db_conf = {
    'engine': create_engine(getenv('DB_URL')),
    'base': declarative_base()
}
