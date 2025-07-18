# Setup.py helps building entire ML Application as a package, even deploy in PyPI
from setuptools import find_packages, setup
from typing import List
HYPEN_E_DOT='-e .'  # This automatically triggers setup.py to build packages

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return a list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name = 'mlproject',
    version='0.0.1',
    author='Rhitwik Prakash',
    author_email='rhitwik.2005@gmail.com',
    packages=find_packages(),
    # install_requires=['pandas','numpy','seaborn'],
    install_requires = get_requirements('requirements.txt')
)


