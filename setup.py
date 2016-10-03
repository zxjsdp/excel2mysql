#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="excel2mysql",
    version='0.0.1',
    description="Export data from Excel to MySQL.",
    long_description=open("README.md").read(),
    author="zxjsdp",
    author_email="zxjsdp@gmail.com",
    packages=find_packages(),
    package_data={"": ["LICENSE"]},
    url="https://github.com/zxjsdp/excel2mysql/",
    tests_require=[
        'pytest==2.5.2',
        'pytest-cov==1.8.1',
        'mock==1.0.1',
    ],
    install_requires=[
        'openpyxl==2.4.0',
    ],
)