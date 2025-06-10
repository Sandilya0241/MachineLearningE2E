import sys
import os
import pandas as pd
import numpy as np

from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
from src.utils import ApplicationConfig
from src.utils import save_object
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join("artifacts","preprocessor.pkl")


class DataTransformation:

    def __init__(self):
        self.__data_transform_obj=DataTransformationConfig()


    def pre_processing(self):
        '''
        This method is pre-processing data before transforming.
        '''
        try:
            logging.info("Data pre-processing started.")

            appCfg = ApplicationConfig().getAppConfig()

            numeric_columns=appCfg.get("config").get("features").get("input_features").get("numerical_features")
            numeric_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler",StandardScaler())
                ]
            )

            categorical_columns=appCfg.get("config").get("features").get("input_features").get("categorical_features")
            categorical_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder",OneHotEncoder()),
                    ("scaler",StandardScaler(with_mean=False))
                ]
            )

            logging.info("Numerical columns standard scaling completed.")
            logging.info("Categorical column encoding completed.")

            preprocessor = ColumnTransformer(
                [
                    ("numeric_pipeline",numeric_pipeline,numeric_columns),
                    ("categorical_pipeline",categorical_pipeline,categorical_columns)
                ]
            )

            return preprocessor


        except Exception as ex:
            raise CustomException(ex,sys)


    def transform_data(self, train_path, test_path):
        '''
        This method is for Transforming data.
        '''
        try:
            logging.info("Data transforming started.")
            
            appCfg = ApplicationConfig().getAppConfig()

            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Reading train and test data completed.")
            logging.info("Obtaining preprocessor object.")
            pre_processing_obj = self.pre_processing()

            target_column_name=appCfg.get("config").get("features").get("target_features")[0]
            target_column_name="math_score"
            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info("Appling preprocessing object on training dataset and test dataset")

            input_feature_train_arr=pre_processing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=pre_processing_obj.transform(input_feature_test_df)
            logging.info("Applied preprocessing object on training dataset and test dataset")
            train_arr=np.c_[
                input_feature_train_arr,np.array(target_feature_train_df)
            ]

            test_arr=np.c_[
                input_feature_test_arr,np.array(target_feature_test_df)
            ]

            logging.info("Data transforming completed.")

            save_object(file_path=self.__data_transform_obj.preprocessor_obj_file_path, obj=pre_processing_obj)

            logging.info("Preprocessor file saved to file successfully.")

            return (train_arr,test_arr,self.__data_transform_obj.preprocessor_obj_file_path)

        except Exception as ex:
            raise CustomException(ex,sys)