#setup.py

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A module where a method or function is passed, along with actions per second.',
    'author': 'Johnny Zhong',
    'url': 'github.com/johnnyczhong/pyrate_limiter',
    'download_url': 'none yet',
    'author_email': 'johnnyczhong@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['rate_limiter'],
    'scripts': [],
    'name': 'Pyrate Limiter'
}

setup(**config)