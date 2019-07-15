import os
from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.develop import develop
import pathlib

NAME = 'git-scan'
DESCRIPTION = "Scan local or remote git repositories for history divergent from origin"
URL = 'https://github.com/johnaparker/git-scan'
EMAIL = 'japarker@uchicago.edu'
AUTHOR = 'John Parker'
KEYWORDS = 'git scan ssh tmux repositories'
VERSION = '0.1'
LICENSE = 'MIT'

REQUIRED = [
    'termcolor', 
    'toml',
    'libtmux',
    'paramiko',
]


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def post_install():
    config_str = """
repositories = [

]""".strip()

    config_path = pathlib.Path('~/.config/git-scan/git-scan.conf').expanduser()
    if not os.path.exists(config_path):
        os.makedirs(config_path.parent, exist_ok=True)
        with open(config_path, 'w') as f:
            f.write(config_str)

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        post_install()
        install.run(self)

class PostDevelopCommand(develop):
    """Post-installation for installation mode."""
    def run(self):
        post_install()
        develop.run(self)

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    license=LICENSE,
    keywords=KEYWORDS,
    url=URL,
    scripts=['git-scan/git-scan'],
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    install_requires=REQUIRED,
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Version Control',
        'Topic :: Software Development :: Version Control :: Git',
    ],
)
