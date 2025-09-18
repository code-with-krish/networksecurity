''''

The setup.py is an essential part of packaging and distributing Python projects. 
It is used by setuptools to define the package metadata and dependencies.

'''



from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """Read the requirements from a file and return them as a list.
    This function will return list of requirements.
    
    """
    requirement_list: List[str] = []
    
    
    try:
        with open("requirements.txt", "r") as file:
            # read all lines from the file
            lines = file.readlines()
            # Process each line to remove whitespace and ignore comments
            for line in lines:
                requirement = line.strip()
                # ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    
    except FileNotFoundError:
        print("requirements.txt file not found")
        
    return requirement_list


setup(
    name ="NetworkSecurity",
    version= "0.0.1",
    author= "Krishna Kanta Maiti",
    author_email= "krishnakantamaiti593@gmail.com",
    packages= find_packages(),
    install_requires= get_requirements(),


    
)


