import os
from dotenv import load_dotenv

load_dotenv(".local.env")

RDS_ENDPOINT = os.environ["RDS_ENDPOINT"]
RDS_USER = os.environ["RDS_USER"]
RDS_PASSWORD = os.environ["RDS_PASSWORD"]
RDS_PORT = os.environ["RDS_PORT"]
RDS_DB_NAME = os.environ["RDS_DB_NAME"]

RDS_POOL_SIZE = int(os.environ["RDS_POOL_SIZE"])
RDS_MAX_OVERFLOW = int(os.environ["RDS_MAX_OVERFLOW"])
RDS_CONNECTION_TIMEOUT = int(os.environ["RDS_CONNECTION_TIMEOUT"])

RDS_URL = (
    f"mysql+pymysql://{RDS_USER}:{RDS_PASSWORD}@{RDS_ENDPOINT}:{RDS_PORT}/{RDS_DB_NAME}"
)
