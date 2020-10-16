#!/usr/bin/python3
from setuptools.command.install import install
from setuptools import setup, find_packages

import jobrun

setup(
    name='jobrun',
    version=jobrun.__version__,
    packages=find_packages(),
    author='Danieł Szczepietilnikow',
    author_email='dshchepetilnikov@gmail.com',
    license='Apache-2.0 License',
    classifiers=[
        'Programming Language :: Python :: 3.5',
    ],
    entry_points={
        'console_scripts': [
            'jobrun = jobrun.cli:main'
        ]
    },
    install_requires=[
        'pyyaml'
    ],
    extras_require={
        'testing': [
            'pytest>=5.0.0',
            'pytest-coverage'
        ]
    },
)
