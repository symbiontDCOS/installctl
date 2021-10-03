from setuptools import setup

setup(
    name='installctl',
    version='0.1.0',
    py_modules=['installctl'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'installctl = installctl:yo_',
        ],
    },
)
