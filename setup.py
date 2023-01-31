from setuptools import find_packages,setup
from typing import List

requirements_filename = "requirements.txt"
REMOVE_PACKAGE = "-e ."

'''
creating the function get_requirements.txt to read the requirements.txt file and replacing the "\n" with nothing 
whitespace because in requirements.txt file by default '\n' is present so basically we 
removing to that.
once you installed -e . via setup.py file there is no imp uses left many more so we can removed it 
from requirements_list file.
'''

def get_requirements() ->List[str]:
    with open(requirements_filename) as requirement_file:
        requirement_list = requirement_file.readline()
    requirement_list = [requirement_name.replace('\n', '') for requirement_name in requirement_list]
    
    if REMOVE_PACKAGE in requirement_list:
        requirement_list.remove(REMOVE_PACKAGE)
    return requirement_list
    

'''
in insurance there has been __init__.py files associated so we 
find packages from that via find_packages and gathering all the requirements via calling the 
function get_requirements
'''

setup(
    name ='Insurance',
    version ='0.0.1',
    description='Insurance Based project',
    author='Bharatbhushan Dwarkewasi',
    author_email='aiwalabro@gmail.com',
    packages= find_packages(), 
    gather_requir = get_requirements()
    )