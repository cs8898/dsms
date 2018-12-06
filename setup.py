#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name='dsms',
    version='0.0.1',
    packages=find_packages(),
    install_requires=['emoji>=0.5.1', 'termcolor>=1.1.0', 'requests>=2.20.1'],
    url='https://github.com/cs8898/dsmsMods',
    license='unlicensed',
    author='Christian Schmied',
    author_email='cs8898@gmx.de',
    description='Dead Simple Monitoring Solution',
    scripts=['dsms']
)
