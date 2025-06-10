import os
import sys

from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object,evaluate_models

from catboost import CatBoostRegressor
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import (GradientBoostingRegressor, AdaBoostRegressor, RandomForestRegressor)
from sklearn.metrics import r2_score

@dataclass
class ModelTrainerConfig:
    trained_model_file_path=os.path.join("artifacts","model.pkl")

class ModelTraining:

    def __init__(self):
        self.__model_trainer_model=ModelTrainerConfig()


    def initiate_model_training(self, train_arr, test_arr):
        try:
            logging.info("Splitting training and test input data")
            X_train, y_train, X_test, y_test = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1],
            )

            models = {
                "Gradient Boosting":GradientBoostingRegressor(),
                "Random Forest":RandomForestRegressor(),
                "Decision Tree":DecisionTreeRegressor(),
                
                "Linear Regression":LinearRegression(),
                # "K-Neighbour Classifier":KNeighborsRegressor(),
                "CatBoost Classifier":CatBoostRegressor(verbose=False),
                "Ada Boost Classifier":AdaBoostRegressor(),
                "XGBClassifier":XGBRegressor()
            }

            logging.info("Finding best model.")
            model_report:dict=evaluate_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,models=models)

            for name, score in model_report.items():
                logging.info(f"Mode Name : {name} and Model Score : {score}")
                
            best_score=max(list(model_report.values()))
            best_model_name=list(model_report.keys())[list(model_report.values()).index(best_score)]
            
            logging.info(f"Best model is {best_model_name} and score is {best_score}")
            best_model=models[best_model_name]
            
            logging.info("Saving the best model object.")
            save_object(self.__model_trainer_model.trained_model_file_path,best_model)
            
            y_pred=best_model.predict(X_test)
            score=r2_score(y_test,y_pred)
            
            return score
        except Exception as ex:
            raise CustomException(ex, sys)

    