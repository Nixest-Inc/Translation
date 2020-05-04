import re
from setuptools import setup

with open('requirements.txt') as f:
    REQUIREMENTS = f.readlines()

with open('README.rst', encoding='utf-8') as f:
    README_RST = f.read()

setup(
    name='translation-wrapper',
    author='Mr.Roxanne',
    url='https://github.com/nixest-Inc/translation',
    version='0.0.1',
    packages=['discord/ext/translation'],
    install_requires=REQUIREMENTS,
    description='System translate bot discord.py',
    long_description=README_RST,
    license='MIT License',
    keywords=['translate','eng','pt-br'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
