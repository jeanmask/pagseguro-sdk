#! /usr/bin/env python
# encoding: utf-8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import pagseguro


REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setup(
    name='Pagseguro SDK',
    version=".".join(map(str, pagseguro.version)),
    description='SDK para utilização do PagSeguro em Python',
    url='https://pagseguro-sdk.readthedocs.com/',
    author='Jean O. Rodrigues',
    author_email='github@jean.bz',
    license='MIT',
    packages=['pagseguro'],
    install_requires=REQUIREMENTS,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
