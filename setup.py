
from setuptools import find_packages, setup

HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str)->list[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as txt_file:
        requirements=txt_file.readlines()
        [req.replace('\n','') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='ds_project_tk',
    version='1',
    author='Tristan Kilper',
    author_email='tristan.kilper@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
