from Insurance.exception import InsuranceException
from Insurance.logger import logging


import os,sys

def test_logger_and_exception():
    try:
        logging.info("starting the logging and exception:")
        result = 3/0
        print(result)
        logging.info("Ending point of  the logging and exception:")
    except Exception as e:
        logging.debug(str(e))
        raise InsuranceException(e, sys)        
    
    
if __name__ == '__main__':
    try:
        test_logger_and_exception()
    except Exception as e:
        print(e)