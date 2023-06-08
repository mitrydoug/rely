from setuptools import find_namespace_package, setup

REQUIREMENTS_FILE = "requirements.in"

def get_requirements(requirements_file):
    pass


setup(
    name='rely',
    version='0.0.1',
    description='Manage dependencies on resources',
    author='Mitchell Douglass',
    author_email='mrdouglass95@gmail.com',
    include_package_data=True,
    package_dir={"": "src"},
    packages=["rely"],
    install_requires=get_requirements(REQUIREMENTS_FILE),
)