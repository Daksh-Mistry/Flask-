# ML Project Setup

when making ml projects we can use this template, it is broader setup template that try's to envolve as many things as possible that is used when working on production envroment.

## Make venv
A critical and first step when making a project is to make venv, it seprates evrything from system and is also used in deployment. <br>
- there are two types of venv used , with conda and with inbuilt python. <br> 

1. with conda we can make evev as follows <br>
  `conda create -p venv python == 3.xx` we can define python version as well <br>
  `conda activate venv/` <br>

2. with python 
   create <br>
   `python3 -m venv venv` <br>
   `. .venv/bin/activate` <br>
- to deactivate use `deactivate`

## Setup git

- Make empy repo in github without .md and anything and copy SSH adress of it. <br>
- initialize and setup git using commands given below. <br>
`git init` <br>
`git add README.md` <br>
`git commit -m "initialize github"` <br>
`git branch -m main` <br>
`git remote add origin "SSH link"` <br>
`git push origin main` <br>

<b> Note : </b> make README.md on local folder and makesure to login with same github id then run all those commands in terminal

## Make Setup.py

This is and importent file that contains project information and setup, it is run before app.py to do initial setup of peoject. <br>

- it contains Setup folder that holds things like name, version, author etc details about project.

#### setup.py
```
from setuptools import setup, find_packages


def get_requirements(path: str = "requirements.txt") -> list:
    '''This function will return the list of requirements'''
    with open(path, "r") as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        requirements.remove('-e .')
    return requirements


setup(
    name = "Flask-Project",
    version = "0.0.1",
    author = "Mistri Daksh",
    author_email = "Myemail@gmail.com",
    packages = find_packages(),
    install_requires= get_requirements('requirements.txt'),
)
```


this automatically downgload `reaquirements.txt` so make sure to create one before running this 

## File Structure

use `templates.py` file to make file structure of project insted of doing it manually, it this left replicate things easily. 
it also makes packages of our project to they can be reused easily for future use. <br>

```
```text
.
├── .env
├── .gitignore
├── .venv/
├── Dockerfile
├── README.md
├── app.py
├── requirements.txt
├── setup.py
├── template.py
├── Data/
├── logs/
├── Test/
└── src/
    └── Project_Name/
        ├── __init__.py
        ├── exception.py
        ├── logger.py
        ├── utils.py
        ├── Components/
        │   ├── __init__.py
        │   ├── data_ingestion.py
        │   ├── data_transformation.py
        │   ├── model_monitoring.py
        │   └── model_trainer.py
        └── Pipelines/
            ├── __init__.py
            ├── prediction_pipeline.py
            └── training_pipeline.py
```

this can easily be build using `template.py`
#### template.py
```
import os
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO)

Project_name = "ML_Project"

files = [
    f'src/{Project_name}/__init__.py',
    f'src/{Project_name}/Components/__init__.py',
    f'src/{Project_name}/Components/data_ingestion.py',
    f'src/{Project_name}/Components/data_transformation.py',
    f'src/{Project_name}/Components/model_trainer.py',
    f'src/{Project_name}/Components/model_monitoring.py',
    f'src/{Project_name}/Pipelines/__init__.py',
    f'src/{Project_name}/Pipelines/training_pipeline.py',
    f'src/{Project_name}/Pipelines/prediction_pipeline.py',
    f'src/{Project_name}/logger.py',
    f'src/{Project_name}/exception.py',
    f'src/{Project_name}/utils.py',
    'setup.py',
    'app.py',
    'Dockerfile'
]

for file in files:
    path = Path(file)
    folder ,_ = os.path.split(path)
    if folder != '':
        os.makedirs(folder, exist_ok=True)
        logging.info(f"Making Folder for {file}")


    if path.exists() :
        logging.info(f'{file} exists')
    else:
        with open(path, 'w') as f :
            pass    
            logging.info(f'When creating file {file}')
```

## Extra files 
some files will not automatically be added such as `.gitignore` see explanation below to setup them and understand components of file strcture. 


## Structure Explanation

This whole things migh seem confusing at first glace but there are just few things to keep in mind in this strcure. <br>

### Root folder's files

- `.gitignore` go on github click add file and paste this name, youll be option to select templete, go and select python in it and make this file.
  it will help iignore venv and outher files that should not be saved into cloud keep away. <br>
- `.env` make manually as per the requirement.
- `Docker` this will be made automatically use it for deployment.
- `app.py` this is the main file that we will run to start exicution of out project

### src / Project
this is a folder where our actual project stays. <br>

#### Components /
- `data_ingesion.py` we make main funciallity here which loads data from data source and saves it for model traning.
- outher components such as for tranformation and prediction also stays here, we use it to handle for our project.

#### Piplines /
two main piplines which are prediction and traning stays here, it isnt used for project exicution. we make ml model here and keep those jupter notebooks in this folder. 

#### Outher files
- `logger.py` we make univeral logger to keep logs of out system here, it will help us keep track of how out app is running.
- `exception.py` to handel exceptions we make univeral handler for easy debugging.
- `utils.py` this file contains basic utilitis that we often use throughout the project to be used easily.

## This isnt absalute blueprint about how we should make our project. this is for better understanding of things that we use in project life cycle. 

# Cookiecutter
- <B> To automate all this we have some inbuilt libraries like `cookiecutter`. checkout that, it also offer some more things that can be used for better project handlig. </B>


### This project also shows how we import data from database in ml project. checkout app.py and trace to know how that happens. :)
