
import os
from pathlib import Path
import logging 

logging.basicConfig(
    level= logging.INFO,
    format = "[%(asctime)s : %(levelname)s]:[%(message)s]"
)

    # enter project name if project name is null then break else continued
while True:
    project_name = input('Enter your project name:')
    if project_name != '':
        break
    
logging.info(f"creating project by name: {project_name}")

list_of_files = [
    "github/workflows/.gitkeep",  # amazon credentials that ignore will keep into .gitkeep 
    "github/workflows/main.yaml", # yaml for creating CICD pipeline
    f"{project_name}/_init__.py",
    f"{project_name}/component/__intit__.py",
    f"{project_name}/entity/__intit__.py",
    f"{project_name}/pipeline/__intit__.py",
    f"{project_name}/config",
    f"{project_name}/exception",
    f"{project_name}/predictor", 
    f"{project_name}/utils.py",
    f"configs/config.yaml",
    "requirements.txt",
    "main.py",
    "setup.py",  
    
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)  # filedir - foldername, filename - inside folder filename
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating a new directory at: {filedir} for filename is: {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"creating a new directory at: {filedir} for filename: {filename}")
            
    else:
        logging.info(f"file  directory already present at: {filepath}")
        
            
    