import logging
import os
from pathlib import Path


project_name = "Text_Summarizer"


list_of_files = [
 "github/workflows/.gitkeep",
 f"src/{project_name}/__init__.py",
 f"src/{project_name}/components/__init__.py",
 f"src/{project_name}/components/utils/__init__.py",
 f"src/{project_name}/utils/commom.py",
 f"src/{project_name}/logging/__init__.py",
 f"src/{project_name}/config/__init__.py",
 f"src/{project_name}/config/configuration.py",
 f"src/{project_name}/pipeline/__init__.py",
 f"src/{project_name}/entity/__init__.py",
 f"src/{project_name}/constants/__init__.py",
 "config/config.yaml",
 "params.yaml",
 "app.py",
 "main.py",
 "Dockerfile",
 "requirements.txt",
 "setup.py",
 "research/trials.ipynp"

]



for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file : {filepath}")

    else:
        logging.info(f"{filepath} already exists")
        