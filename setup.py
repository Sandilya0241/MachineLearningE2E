from setuptools import find_packages, setup
from typing import List
HYPHEN_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements.
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[requirement.replace("\n","") for requirement in requirements if HYPHEN_DOT!=requirement]
    
    print(requirements)
    return requirements

setup(
    name='MachineLearningE2E',
    version='1.0.0',
    author='Sandilya S',
    author_email='SANDYCODESEARCH@GMAIL.COM',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)