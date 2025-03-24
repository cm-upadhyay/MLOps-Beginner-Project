import sys
import pandas as pd
import numpy as np
from typing import Optional

from src.configuration.mongo_db_connection import MongoDBClient
from src.constants import DATABASE_NAME
from src.exception import MyException

class Proj1Data:
    """
    A data access class that handles exporting MongoDB collections to pandas DataFrames.
    Provides methods to connect to MongoDB and transform collection data into analysis-ready DataFrames.
    """

    def __init__(self) -> None:
        """
        Initializes MongoDB client connection using the default database name.
        
        Raises:
            MyException: If connection to MongoDB fails
        """
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
        except Exception as e:
            raise MyException(e, sys)

    def export_collection_as_dataframe(
        self, 
        collection_name: str, 
        database_name: Optional[str] = None
    ) -> pd.DataFrame:
        """
        Exports a MongoDB collection to a pandas DataFrame with data cleaning.
        
        Args:
            collection_name: Name of the MongoDB collection to export
            database_name: Optional database name (uses default if None)
            
        Returns:
            pd.DataFrame: Cleaned DataFrame with:
                - MongoDB '_id' field removed
                - 'na' strings converted to np.nan
                
        Raises:
            MyException: If data export or transformation fails
            
        Example:
            >>> data_exporter = Proj1Data()
            >>> df = data_exporter.export_collection_as_dataframe("my_collection")
        """
        try:
            # Access specified collection from the default or specified database
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]

            # Convert entire collection to DataFrame
            print("Fetching data from MongoDB...")
            df = pd.DataFrame(list(collection.find()))
            print(f"Successfully fetched {len(df)} records")
            
            # Data cleaning steps
            if "_id" in df.columns:
                df = df.drop(columns=["_id"], axis=1)  # Remove MongoDB ObjectId
            df.replace({"na": np.nan}, inplace=True)  # Standardize missing values
            
            return df

        except Exception as e:
            raise MyException(e, sys)