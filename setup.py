from setuptools import setup, find_packages

setup(
    name='src',
    version = '0.0.1',
    author = 'Nidhi Tank',
    author_email = "ntank2024@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"}
)