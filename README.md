# Anotation-Converter

## Setting up the environments

step 1: Create the new python environment using following command

		conda create -n <environment_name> python=3.7

step 2: Once new environment created activate using following command

		conda activate <environment_name>

step 3: Once environment is activate using requirements.txt to install all packages using following command

		pip install -r requirements.txt
    
##  How to run the main.py

To run main.py file you will need to set hyperparameter needs to use in main.py file which are at config\hyp.yaml (follow hyp.yaml from that folder to know more). once you finished setting them up use following command to starts model training:

    python main.py
    
Once conversion is finished you can see all converted annotations in the output folder.
