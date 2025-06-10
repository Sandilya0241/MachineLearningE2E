import yaml
import sys
import os
import dill
from src.exception import CustomException
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score

class ApplicationConfig(object):
    __appConfig = {}

    def __new__(cls):
        if not hasattr(cls,'instance'):
            try:
                cls.instance=super(ApplicationConfig, cls).__new__(cls)
                with open("AppConfig.yaml","r") as fp:
                    cls.__appConfig=yaml.safe_load(fp)
            except Exception as ex:
                raise CustomException(ex, sys)
        return cls.instance
    
    def getAppConfig(self):
        return self.__appConfig
    

def save_object(file_path, obj):
    '''
    This function is useful in saving an object in the specified file path
    '''
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)
    except Exception as ex:
        raise CustomException(ex, sys)
    

def evaluate_models(X_train,y_train,X_test,y_test,models):
    '''
    This function is useful in evaluating models and collecting it's respective R2 score.
    '''
    try:
        
        appCfg = ApplicationConfig().getAppConfig()
        params=appCfg.get("config").get("params")
        model_report = {}
        
        for key, model in models.items():
            # model.fit(X_train,y_train)
            param=params[key]
            if param is None:
                param={}
            gridCV = GridSearchCV(model,param_grid=param,cv=3)
            gridCV.fit(X_train,y_train)

            model.set_params(**gridCV.best_params_)
            model.fit(X_train,y_train)

            y_train_pred=model.predict(X_train)
            train_score = r2_score(y_train,y_train_pred)

            y_test_pred=model.predict(X_test)
            test_score = r2_score(y_test,y_test_pred)

            model_report[key]=test_score

        return model_report
        
    except Exception as ex:
        CustomException(ex, sys)
