#!/usr/bin/env python

from setuptools import setup, find_packages, Extension
from glob import glob

sources = glob('WiringOP/devLib/*.c')
sources += glob('WiringOP/wiringPi/*.c')
sources += ['wiringpi_wrap.c']

sources.remove('WiringOP/devLib/piFaceOld.c')

_wiringpi = Extension(
    '_wiringpi',
    include_dirs=['WiringOP/wiringPi','WiringOP/devLib'],
    sources=sources
)

setup(
    name = 'wiringpi',
    version = '2.32.1',
    author = "Philip Howard",
    author_email = "phil@gadgetoid.com",
    url = 'https://github.com/WiringPi/WiringPi-Python/',
    description = """A python interface to WiringPi 2.0 library which allows for
    easily interfacing with the GPIO pins of the Raspberry Pi. Also supports
    i2c and SPI""",
    long_description=open('README.md').read(),
    ext_modules = [ _wiringpi ],
    py_modules = ["wiringpi"],
    install_requires=[],
    headers=glob('WiringOP/wiringPi/*.h')+glob('WiringOP/devLib/*.h')
)
