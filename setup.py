from setuptools import setup, find_packages
import seleniumhelper

VERSION = seleniumhelper.__version__

setup(name="seleniumhelper", version=VERSION, packages=find_packages())
