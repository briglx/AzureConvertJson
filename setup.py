#!/usr/bin/env python3
"""Convert Json."""
from setuptools import find_packages, setup

PACKAGES = find_packages(exclude=["tests", "tests.*"])

setup(
    name="Convert Json",
    version="0.0.1",
    packages=PACKAGES,
)
