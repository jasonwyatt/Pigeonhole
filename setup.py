import os
from setuptools import setup, find_packages

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name = "pigeonhole",
    version = "0.1.0",
    author = "Jason Feinstein",
    author_email = "jason.feinstein@gmail.com",
    description = (
        "A visual tool that can be used to allow you to easily classify training, validation, and test data for machine learning applications."
    ),
    long_description=read('USAGE_README.md'),
    keywords = "machine-learning server training classification",
    packages = find_packages(),
    scripts = ['bin/pigeonhole'],
    install_requires = read('requirements.txt'),
    include_package_data = True,
    zip_safe = False,
    license = "GPL",
    classifiers = [
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Utilities',
    ],
)