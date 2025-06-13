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

## Agenda - Docker ECR EC2
* Docker Build Check
* Github workflow
* IAM user creation in AWS
* Create ECR repository
* Create EC2 Instance
* Run below commands in EC2 instance  
~~~
sudo apt-get update -y  
sudo apt-get upgrade  
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker

check docker is running or not with command "docker"

Goto GITHUB repo and settings and goto Actions Runner tab.
Create a new runnuer and select "Linux".
Execute below commands

Download:

# Create a folder
$ mkdir actions-runner && cd actions-runner# Download the latest runner package
$ curl -o actions-runner-linux-x64-2.325.0.tar.gz -L https://github.com/actions/runner/releases/download/v2.325.0/actions-runner-linux-x64-2.325.0.tar.gz# Optional: Validate the hash
$ echo "5020da7139d85c776059f351e0de8fdec753affc9c558e892472d43ebeb518f4  actions-runner-linux-x64-2.325.0.tar.gz" | shasum -a 256 -c# Extract the installer
$ tar xzf ./actions-runner-linux-x64-2.325.0.tar.gz


Configure:
# Create the runner and start the configuration experience
$ ./config.sh --url https://github.com/Sandilya0241/MachineLearningE2E --token AIFN2LNO4L23Q6ZFMK25E6TIJQC4C# Last step, run it!
$ ./run.sh

Using your self-hosted runner:
# Use this YAML in your workflow file for each job
runs-on: self-hosted
~~~