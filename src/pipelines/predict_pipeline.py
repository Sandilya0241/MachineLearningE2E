import os
import sys
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object


class PredictPipeline:
    def __init__(self,data_frame):
        self._df=data_frame

    def predict(self):
        try:
            prepocessing_filepath=os.path.join("artifacts","preprocessor.pkl")
            model_filepath=os.path.join("artifacts","model.pkl")

            preprocessing=load_object(file_path=prepocessing_filepath)
            model=load_object(file_path=model_filepath)

            features_scaled=preprocessing.transform(self._df)
            results=model.predict(features_scaled)

            return results
            
        except Exception as ex:
            raise CustomException(ex,sys)

class StudentData:
    def __init__(self,
                 gender:str,
                 race_ethnicity:str,
                 parental_level_of_education:str,
                 lunch:str,
                 test_preparation_course:str,
                 reading_score:int,
                 writing_score:int):
        self.gender=gender
        self.race_ethnicity=race_ethnicity
        self.parental_level_of_education=parental_level_of_education
        self.lunch=lunch
        self.test_preparation_course=test_preparation_course
        self.reading_score=reading_score
        self.writing_score=writing_score


    def get_data_as_data_frame(self):
        try:
            input = {
                "gender":[self.gender],
                "race_ethnicity":[self.race_ethnicity],
                "parental_level_of_education":[self.parental_level_of_education],
                "lunch":[self.lunch],
                "test_preparation_course":[self.test_preparation_course],
                "reading_score":[self.reading_score],
                "writing_score":[self.writing_score],
            }
            dataframe=pd.DataFrame(input)
            return dataframe
        except Exception as ex:
            raise CustomException(ex,sys)