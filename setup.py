#!/usr/bin/env python3
from setuptools import setup, find_packages
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='dsms',
    version='0.0.2',
    packages=find_packages(),
    install_requires=['emoji>=0.5.1', 'termcolor>=1.1.0', 'requests>=2.20.1'],
    url='https://github.com/cs8898/dsmsMods',
    license='unlicensed',
    author='Christian Schmied',
    author_email='cs8898@gmx.de',
    description='Dead Simple Monitoring Solution',
    long_description=long_description,
    long_description_content_type='text/markdown',
    scripts=['dsms']
)
