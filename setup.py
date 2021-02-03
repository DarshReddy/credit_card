import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='credit_card',
    version='1.3',
    url='https://github.com/darshreddy/credit_card',
    author='Darsh Reddy',
    keywords='creditcard',
    description='Set of classes for validating, identifying and formatting do credit cards.',
    packages=find_packages(),
    install_requires=[],
    test_suite='tests',
    setup_requires=['pytest-runner', ],
    tests_require=['pytest', ],
    include_package_data=True,
    long_description=README,
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
)