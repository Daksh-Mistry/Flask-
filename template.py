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
    f'src/{Project_name}/components/model_monitoring.py',
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