from setuptools import setup, find_packages
from pkg_resources import parse_requirements
import pathlib
import sys

with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in parse_requirements(requirements_txt)
    ]

VERSION = "0.0.1rc0"

if '--version' in sys.argv:
    version = sys.argv.index('--version')
    sys.argv.pop(version)
    VERSION = sys.argv.pop(version)


# read the contents of README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='azdiff',
    version=VERSION,
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'azdiff=src.main:cli',
        ],
    },
    packages=find_packages(),
    url='https://github.com/RachidAZ/AzDiff',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    author='Rachid Azgaou',
    author_email='rachid.azgaou.us@gmail.com',
    python_requires=">=3.8",
    description='Azure resources configuration differences',
    readme = "README.md",
    long_description=long_description,
    long_description_content_type='text/markdown'
)

