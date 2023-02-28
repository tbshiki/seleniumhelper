from setuptools import setup, find_packages

NAME = "seleniumhelper"
AUTHOR = "tbshiki"
AUTHOR_EMAIL = "info@tbshiki.com"
URL = "https://github.com/tbshiki/seleniumhelper"
VERSION = "0.1.1"
PYTHON_REQUIRES = ">=3.9"
INSTALL_REQUIRES = [
    "selenium>=4.8.0",
    "platform",
    "time",
    "os",
]


setup(name=NAME, author=AUTHOR, author_email=AUTHOR_EMAIL, version=VERSION, python_requires=PYTHON_REQUIRES, install_requires=INSTALL_REQUIRES, packages=find_packages())
