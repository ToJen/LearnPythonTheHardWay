try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Tomisin',
    'url':   'https://www.github.com/ToJen',
    'download_url': 'none bruh!',
    'author_email': 'my@mail.null',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages':    ['EXAMPLE'],
    'scripts': [],
    'name': 'example'
}

setup(**config)
