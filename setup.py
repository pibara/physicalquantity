from setuptools import setup, find_packages
from codecs import open
from os import path
from sys import platform
here = path.abspath(path.dirname(__file__))

setup(
    name='physicalquantity',
    version='0.0.1',
    description='Simple library for working with physical quantities',
    long_description="""A simple library for working with physical quantities. 
    Implements basic dimensional decomposition of physical quantities and provides
    basic operations (adition, subtraction, multiplication, division, comparison) 
    for working with these quantities.

    Support for non-SI units is currently partialy supported, better support in under way. 

    """,
    url='https://github.com/pibara/aioflureedb',
    author='Rob J Meijer',
    author_email='pibara@gmail.com',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Environment :: Other Environment'
    ],
    keywords='units quantities',
    packages=find_packages(),
)

