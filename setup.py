from setuptools import setup, find_packages
import seleniumhelper

NAME = "seleniumhelper"
AUTHOR = "tbshiki"
AUTHOR_EMAIL = "info@tbshiki.com"
URL = "https://github.com/tbshiki/seleniumhelper"
VERSION = seleniumhelper.__version__
PYTHON_REQUIRES = ">=3.9"
INSTALL_REQUIRES = [
    "selenium>=4.8.0",
    "platform",
    "time",
    "os",
]


setup(name=NAME, author=AUTHOR, author_email=AUTHOR_EMAIL, version=VERSION, python_requires=PYTHON_REQUIRES, install_requires=INSTALL_REQUIRES, packages=find_packages())
