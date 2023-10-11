from setuptools import setup, find_packages

NAME = "seleniumhelper"
VERSION = "0.1.2"
PYTHON_REQUIRES = ">=3.9"
INSTALL_REQUIRES = [
    "selenium>=4.8.0",
]

AUTHOR = "tbshiki"
AUTHOR_EMAIL = "info@tbshiki.com"
URL = "https://github.com/tbshiki/" + NAME


setup(
    name=NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    version=VERSION,
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(),
)
