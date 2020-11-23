# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in sungas_app/__init__.py
from sungas_app import __version__ as version

setup(
	name='sungas_app',
	version=version,
	description='Sungas customization',
	author='Anthony Emmanuel C.',
	author_email='mymi14s@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
