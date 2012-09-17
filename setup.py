import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "quickchart",
    version = "0.0.1",
    author = "Marcin Karkocha",
    author_email = "kivio@kivio.pl",
    description = ("QuickChart is a lightweight library for drawing graphs and tables "
                   "using just PIL."),
    license = "Apache Software License 2.0",
    keywords = "charts tables graphs",
    url = "https://github.com/kivio/python-quickchart",
    packages=['declarative', 'drawing','examples','simple','tests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 2.7",
        "Topic :: Utilities",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Software Development :: Libraries :: Python Modules"
        ],
)
