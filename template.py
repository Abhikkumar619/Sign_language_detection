import os
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "signLanguage"


list_of_files = [
    ".github/workflows/.gitkeep",
    "data/.gitkeep",
    "docs/.gitkeep",

    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/s3_operations.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/training_pipeline/__init__.py",
    f"{project_name}/constant/application.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifacts_entity.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "template/index.html",
    ".dockerignore",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"


]

for path in list_of_files: 
    dir_name, file_name=os.path.split(path)
    
    # logging.info(f"directories name: {dir_name} and file name : {file_name}")
    
    if dir_name != "": 
        os.makedirs(dir_name, exist_ok=True)
        logging.info(f"Directory {dir_name} is created for file {file_name}")
        
    if (not os.path.exists(path)) or (os.path.getsize(path) == 0): 
        with open(path, 'w') as f: 
            pass
        logging.info(f"file is created {file_name}")
    else: 
        logging.info(f"File is already created")
        
        
        