from datetime import datetime
from genericpath import exists
import os
import logging

LOG_DIR = "Insurance log"

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
LOG_FILE_NAME = F"log_{CURRENT_TIME_STAMP}.log"
os.makedirs(LOG_DIR, exist_ok = True)
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

logging.basicConfig(
    filename= LOG_FILE_PATH,
    filemode= 'w',
    format= '[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    # level= logging.INFO
    level= logging.DEBUG
    )
'''
whatever the info you need you can ask by level , if you need all the info all debug used debug,
if you need only information then you can logging.info
'''