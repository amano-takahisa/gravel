#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'GDAL>=3.4.2'
    # 'fiona>=1.8.21',
    # 'pyproj>=3.3.0',
    # 'shapely>=1.8',
    # 'geopandas>=0.10.2'
]

test_requirements = [
    'pytest>=3', ]

setup(
    author="Amano Takahisa",
    author_email='amano.takahisa@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="my personal project",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='gravel',
    name='gravel',
    packages=find_packages(include=['gravel', 'gravel.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/amano-takahisa/gravel',
    version='0.1.0',
    zip_safe=False,
)
