# -*- coding: utf-8 -*-
# (c) Copyright 2021 Sensirion AG, Switzerland

from __future__ import absolute_import, division, print_function
from setuptools import setup, find_packages
import os
import re


# Read version number from version.py
version_line = open("sensirion_i2c_svm41/version.py", "rt").read()
result = re.search(r"^version = ['\"]([^'\"]*)['\"]", version_line, re.M)
if result:
    version_string = result.group(1)
else:
    raise RuntimeError("Unable to find version string")


# Use README.rst and CHANGELOG.rst as package description
root_path = os.path.dirname(__file__)
readme = open(os.path.join(root_path, 'README.rst')).read()
changelog = open(os.path.join(root_path, 'CHANGELOG.rst')).read()
long_description = readme.strip() + "\n\n" + changelog.strip() + "\n"


setup(
    name='sensirion-i2c-svm41',
    version=version_string,
    author='Philippe Largier',
    author_email='info@sensirion.com',
    description='I2C Driver for Sensirion SVM41 Evaluation Kit',
    license='BSD',
    keywords='sensirion i2c driver svm41',
    url='https://github.com/sensirion/python-i2c-svm41',
    packages=find_packages(exclude=['tests', 'tests.*']),
    long_description=long_description,
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',
    install_requires=[
        'sensirion-i2c-driver~=1.0.0',
    ],
    extras_require={
        'test': [
            'flake8~=3.9.2',
            'mock~=3.0.0',
            'pytest~=6.2.5',
            'pytest-cov~=3.0.0',
            'sensirion-shdlc-sensorbridge~=0.1.1',
        ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: System :: Hardware :: Hardware Drivers'
    ]
)
