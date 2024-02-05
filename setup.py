from setuptools import setup, find_packages

setup(
    name='myplotpkg',
    version='0.1.0',
    author='birchtree2',
    author_email='',
    description='A simple Python package for data visualization with matplotlib.',
    packages=find_packages(),
    install_requires=[
       'numpy',
       'matplotlib',
       'scipy',
    ],
)