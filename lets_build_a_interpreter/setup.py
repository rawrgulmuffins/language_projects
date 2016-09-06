from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

with open("build_requires.txt") as file:
    install_requires = [dep.strip() for dep in file.readlines()]

setup(
    name='pascal_interpreter',
    description='Toy Pascal Interpreter.',
    version='0.0.1',
    long_description='',
    url='https://github.west.isilon.com/alord/scatter_gather_grep',
    author='Alex LordThorsen',
    author_email='alord@isilon.com',
    license='ISCL',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Business Information',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='',
    packages=find_packages(include=['pascal_interpreter']),
    py_modules=[],
    install_requires=install_requires,
)
