# Copyright (c) 2018 The Regents of the University of Michigan
# All rights reserved.
# This software is licensed under the BSD 3-Clause License.
import os
from setuptools import setup, find_packages

description = 'Data visualization based on signac.'

try:
    this_path = os.path.dirname(os.path.abspath(__file__))
    fn_readme = os.path.join(this_path, 'README.md')
    with open(fn_readme) as fh:
        long_description = fh.read()
except (IOError, OSError):
    long_description = description


setup(
    name='signac-dashboard',
    version='0.1.6',
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.4',
    install_requires=[
        'signac>=0.8',
        'Flask>=0.12',
        'Flask-Assets',
        'webassets>=0.12.1',
        'Flask-Turbolinks',
        'libsass',
        'jsmin'
    ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    author='Bradley Dice',
    author_email='bdice@bradleydice.com',
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='visualization dashboard signac framework',
    url='https://bitbucket.org/glotzer/signac-dashboard',

    entry_points={
        'console_scripts': [
            'signac-dashboard = signac_dashboard.__main__:main',
        ],
    },
)
