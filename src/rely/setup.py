from setuptools import setup

REQUIREMENTS_FILE = "requirements.in"

def get_requirements(requirements_file):
    pass


setup(
    name='rely',
    version='0.0.1',
    description='Manage dependencies on resources',
    author='Mitchell Douglass',
    author_email='mrdouglass95@gmail.com',
    install_requires=get_requirements(),
)