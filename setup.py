import sys

from setuptools import setup, find_packages

if sys.version_info.major != 3:
	raise RuntimeError("This package requires Python 3+")

# https://caremad.io/2013/07/setup-vs-requirement/

with open('./requirements.txt') as r:
	requirements = [line for line in r]

with open("README.md", "r") as fh:
	long_description = fh.read()

setup(
	name='py-rclone',
	version='0.0.1',
	url='https://github.com/Onemind-Services-LLC/py-rclone',
	description='Python client for rClone',
	long_description=long_description,
	long_description_content_type="text/markdown",
	install_requires=requirements,
	classifiers=[
		'Intended Audience :: Developers',
		'Programming Language :: Python :: 3.9',
		'Programming Language :: Python :: 3.10',
		'Topic :: Software Development :: Libraries',
	],
	packages=find_packages(include=['oms', 'oms.rclone'])
)
