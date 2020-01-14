"""
setup.py for project jupiter
"""

import os
import setuptools

here = os.path.abspath(os.path.dirname(__file__))

description = "project jupiter"

with open(os.path.join(here, 'README.md')) as f:
  long_description = f.read()

setuptools.setup(
    name = 'jupiter',
    version = '0.0.0',
    description = description,
    long_description = long_description,
    packages = setuptools.find_packages()
)
