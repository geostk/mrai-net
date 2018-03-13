from distutils.core import setup
from setuptools import find_packages
from os.path import join, dirname


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


with open(join(dirname(__file__), 'mrai/_version.py')) as versionpy:
    exec(versionpy.read())

with open('requirements.txt') as reqsfile:
    required = reqsfile.read().splitlines()

setup(
    name='mrai',
    version=__version__,
    description=("MR acquisition-invariant representation learning."),
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=required,
    url="https://github.com/wmkouw/mrai-net",
    license='Apache 2.0',
    author='Wouter Kouw',
    author_email='wmkouw@gmail.com',
    classifiers=['Topic :: Machine Learning :: classifiers',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python']
)
