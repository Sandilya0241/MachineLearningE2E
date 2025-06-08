import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass

@dataclass
class DataInjestionConfig:
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")
    raw_data_path:str=os.path.join("artifacts","data.csv")


class DataInjestion:
    def __init__(self):
        self.injestion_config=DataInjestionConfig()

    def initiate_data_injestion(self):
        """
        This method will do Data Injestion part.
        """
        try:
            logging.info("Data Injestion started.")
            df=pd.read_csv("notebook\\data\\stud.csv")

            logging.info("Creating directories for artifacts.")
            os.makedirs(os.path.dirname(self.injestion_config.train_data_path),exist_ok=True)

            logging.info("Read the dataset as a DataFrame.")
            df.to_csv(self.injestion_config.raw_data_path,index=False,header=True)
            
            logging.info("Implementing Train Test Split functionality.")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.injestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.injestion_config.test_data_path,index=False,header=True)
            logging.info("Data Injestion completed.")

            return (
                self.injestion_config.train_data_path,
                self.injestion_config.test_data_path
            )
        except Exception as ex:
            raise CustomException(ex, sys)