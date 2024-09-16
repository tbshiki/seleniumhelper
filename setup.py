from setuptools import setup, find_packages

NAME = "seleniumhelper"
VERSION = "0.2.1"
PYTHON_REQUIRES = ">=3.9"
INSTALL_REQUIRES = ["selenium>=4.8.0"]

AUTHOR = "tbshiki"
AUTHOR_EMAIL = "info@tbshiki.com"
URL = "https://github.com/tbshiki/" + NAME

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    description="A helpful utility wrapper for Selenium WebDriver.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="selenium, automation, webdriver, operation",
)
