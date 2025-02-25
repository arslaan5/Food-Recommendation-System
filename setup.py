from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    """Get the list of requirements from a file."""
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if (HYPHEN_E_DOT) in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements


setup(
    name='Food Recommender System', 
    version='0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    author='Arslaan Siddiqui',
    author_email='arslaansiddiqui23@gmail.com',
    description='This a food recommender system that uses content-based filtering to recommend food items to users based on their previous ratings.',
    license='Apache 2.0',
)