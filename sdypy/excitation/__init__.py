"""
A project template for the SDyPy effort..
"""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("sdypy-excitation")
except PackageNotFoundError:  # source checkout without installed metadata
    __version__ = "0+unknown"

from pyExSi import *
