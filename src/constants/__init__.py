import os
from datetime import date

# MongoDB Configuration Constants
DATABASE_NAME = "Proj1"  
COLLECTION_NAME = "Proj1-Data"
MONGODB_URL_KEY = "MONGODB_URL"  # Environment variable key for MongoDB connection URL

# Project Pipeline Configuration
PIPELINE_NAME: str = ""  # Name of the ML pipeline (to be specified)
ARTIFACT_DIR: str = "artifact"  # Directory to store pipeline artifacts

# Model Configuration
MODEL_FILE_NAME = "model.pkl"  # Filename for saved model
TARGET_COLUMN = "Response"  # Target variable for ML model
CURRENT_YEAR = date.today().year  # Current year for time-based features
PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl"  # Filename for preprocessing object

# Data File Configuration
FILE_NAME: str = "data.csv"  # Raw data filename
TRAIN_FILE_NAME: str = "train.csv"  
TEST_FILE_NAME: str = "test.csv"  
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")  # Path to schema definition file

# AWS Configuration
AWS_ACCESS_KEY_ID_ENV_KEY = "AWS_ACCESS_KEY_ID" 
AWS_SECRET_ACCESS_KEY_ENV_KEY = "AWS_SECRET_ACCESS_KEY"  
REGION_NAME = "us-east-1" 

# Data Ingestion Configuration
DATA_INGESTION_COLLECTION_NAME: str = "Proj1-Data"  # Source collection for data ingestion
DATA_INGESTION_DIR_NAME: str = "data_ingestion"  # Directory for ingestion artifacts
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"  # Directory for raw feature storage
DATA_INGESTION_INGESTED_DIR: str = "ingested"  # Directory for processed data
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.25  # Test set size ratio (25%)

APP_HOST = "0.0.0.0"
APP_PORT = 5000