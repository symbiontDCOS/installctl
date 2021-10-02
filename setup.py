"""
Setup for installctl application
"""
from setuptools import setup, find_packages

setup(
    name='installctl',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'installctl = installctl.scripts.installctl:cli',
        ],
    },
)
