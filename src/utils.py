import yaml
import sys
import os
import dill
from src.exception import CustomException

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
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)
    except Exception as ex:
        raise CustomException(ex, sys)