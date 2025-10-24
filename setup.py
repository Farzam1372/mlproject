from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str)->list[str]:
    ''''
    This function will return the list of requirements
    '''
    HYPEN_E_DOT = '-e .'
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='End to End ML project',
    version='0.1',
    author='Farzam',
    author_email='farzamnazari.mec@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)