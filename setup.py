# Import the `setup` function and `find_packages` utility from setuptools
from setuptools import setup, find_packages

# Call the `setup` function to define the project's metadata
setup(
    name="src",  # Name of the project
    version="0.0.1",  # Version of the project
    author="CM upadhyay",  # Author's name
    author_email="upadhyay.chandramohan@gmail.com",  # Author's email
    packages=find_packages()  # Automatically find and include all Python packages
)