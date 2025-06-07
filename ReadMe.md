## Agenda - E2E project
* Setup the GitHub repository
    * Create a new environment.
        '''conda create -p venv python==3.12.7 -y  
        conda activate venv/  
        git init  
        git add README.md  
        git commit -m "first commit"
        git branch -M main  
        git remote add origin https://github.com/Sandilya0241/MachineLearningE2E.git  
        git push -u origin main'''
    * setup.py -> Project setup
        * This file will help our code to work as package (pip install) or use it in other programs.
	* requirements.txt file - This file is needed to install as part of project.
* Added src folder and build 
* Create components that deals with Data Ingestion, Data Transformation, and Model Trainer Functionalities.
* Create pipeline to Train the models and to Predict output.
* Add a file for Common Utility Functions, Logging, and Exception Handling. 