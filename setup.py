# from setuptools import find_packages, setup
# from typing import List

# HYPHEN_E_DOT='-e .'
# def get_requirements(file_path:str)->List[str]:
#     '''
#     this function return the list of requirements
#     '''
#     requirements=[]
#     with open(file_path) as file_obj:
#         requirements=file_obj.readlines()
#         requirements=[req.replace("\n","") for req in requirements]
#         if HYPHEN_E_DOT in requirements:
#             requirements.remove(HYPHEN_E_DOT)

#     return requirements    
 
# ## meta-data information about the entire project 
# setup(
# name='MLProject',
# version='0.0.1',
# author='Shreya',
# author_email='shreyachauhan0513@gmail.com',
# packages=find_packages(),
# install_requires=get_requirements('requirements.txt')


# )
from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns the list of requirements.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

## Meta-data information about the entire project
setup(
    name='MLProject',
    version='0.0.1',
    author='Shreya',  # Fixed typo here
    author_email='shreyachauhan0513@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
