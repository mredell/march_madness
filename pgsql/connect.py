import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect

# Load environment variables
load_dotenv()

# Database connection details
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

# Create database engine
engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Test Connection
def get_engine():
    try:
        with engine.connect() as connection:
            print("✅ Successfully connected to the PostgreSQL database!")
        return engine
    except Exception as e:
        raise e
    
