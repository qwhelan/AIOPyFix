import os

from setuptools import setup, Extension
from Cython.Build import cythonize

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


config = {
    'description': 'aiopyfix',
    'author': 'Maksim Afanasevsky',
    'url': 'https://github.com/maxtwen/AIOPyFix/',
    'download_url': 'https://github.com/maxtwen/AIOPyFix/',
    'author_email': 'maxtwen1@gmail.com',
    'version': '0.4',
    'install_requires': ['cython'],
    'packages': ['aiopyfix', 'aiopyfix.FIX44'],
    'scripts': [],
    'name': 'aiopyfix',
    'long_description': read('README.md'),
    'long_description_content_type': 'text/markdown',
    'ext_modules': cythonize([Extension(f"aiopyfix.utils", ["aiopyfix/utils.pyx"])]),
}

setup(**config)
