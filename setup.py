#!/usr/bin/env python3

import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='ffpass',
    version='0.2.1',
    author='Louis Abraham',
    license='MIT',
    author_email='louis.abraham@yahoo.fr',
    description='Import and Export passwords for Firefox',
    long_description=read('README.rst'),
    url='https://github.com/louisabraham/ffpass',
    use_scm_version=False,
    install_requires=['pyasn1', 'Crypto'],
    python_requires='>=3',
    entry_points={'console_scripts': ['ffpass = ffpass:main']},
    classifiers=[
        'Topic :: Utilities',
        'Topic :: Security :: Cryptography'
    ],
)