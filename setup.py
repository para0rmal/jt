import os
import re
import sys

from setuptools import setup, find_packages

install_requires = [
    'click',
    'requests',
    'PyYAML>5.1',
    'colr',
    'asciitree'
]

setup(
    name = 'jt',
    version = '1.0',
    long_description = 'A command line utility which allows you to visualise the nodes in a JSON file (or GET request) as an ASCII tree.',
    platforms = 'Fedora 26',
    license = 'MIT',
    url = 'https://github.com/para0rmal/jt',
    author = 'Horia-Emanuel Muntean',
    author_email = 'para0rmal@gmail.com',
    packages = find_packages(),
    install_requires = install_requires,
    setup_requires = [],
    tests_require = ['pytests', 'responses'],
    zip_safe = True,
    entry_points = '''
        [console_scripts]
        jt=jt:main
    '''
)
