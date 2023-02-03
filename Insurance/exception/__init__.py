from fileinput import filename
from logging import Logger
import os
import sys

class InsuranceException(Exception):
    def __init__(self, error_message:Exception, error_detail:sys):
        super().__init__(error_message)
        self.error_message = InsuranceException.error_message_detail(error_message,error_detail=error_detail)
    
    @staticmethod    # to rerun the function we called static method.    
    def error_message_detail(error_message:Exception, error_detail:sys)->str:
        _,_, exc_tb = error_detail.exc_info()
        line_number = exc_tb.tb_frame.f_lineno
        
        filename = exc_tb.tb_frame.f_code.co_filename
        
        # preparing error message
        error_message = f"error ocurred python scripts name {filename}" \
                        f"error ocurred at linenumber[{exc_tb.tb_lineno}] error message [{error}]."
                        
        return error_message
    
    def __str__(self) -> str:
        return InsuranceException.__name__.__str__()