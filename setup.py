from setuptools import setup, find_packages


def get_requirements(path: str = "requirements.txt") -> list:
    '''This function will return the list of requirements'''
    with open(path, "r") as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        requirements.remove('-e .')
    return requirements


setup(
    name = "Flask-Project",
    version = "0.0.1",
    author = "Mistri Daksh",
    author_email = "Myemail@gmail.com",
    packages = find_packages(),
    install_requires= get_requirements('requirements.txt'),
)