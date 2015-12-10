from setuptools import setup

import os


# Installed name used for various commands (both script and setuptools).
command_name = 'webserver_test_application'

with open('README.md') as file:
        long_description = file.read()

with open('dev_requirements.txt') as file:
    tests_require = [dep.strip() for dep in file.readlines()]

required_packages = []

setup(name='bugs_to_githubs',
      version='0.0.1',
      description='Test application for all language web server implementation.',
      long_description=long_description,
      author='Alex LordThorsen',
      author_email='alexlordthorsen@gmail.com',
      url='',
      include_package_data=True,
      install_requires=required_packages,
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
      ],
      zip_safe=True,
)
