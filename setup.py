import sys

from setuptools import setup


def read_file(fname):
    with open(fname) as f:
        return f.read()


setup(
    name='pytest-testrail',
    description='pytest plugin for creating TestRail runs and adding results',
    long_description=read_file('README.rst'),
    version='1.0.0',
    author='Allan Kilpatrick',
    author_email='allanklp@gmail.com',
    url='http://github.com/allankilpatrick/pytest-testrail/',
    packages=[
        'pytest_testrail',
    ],
    package_dir={'pytest_testrail': 'pytest_testrail'},
    install_requires=[
        'pytest==3.1.2',
        'requests==2.18.1',
        'simplejson==3.11.1',
    ],
    include_package_data=True,
    entry_points={'pytest11': ['pytest-testrail = pytest_testrail.conftest']},
)
