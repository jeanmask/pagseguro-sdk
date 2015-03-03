#! /usr/bin/env python
# encoding: utf-8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import pagseguro


setup(
    name='Pagseguro SDK',
    version=pagseguro.version,
    description='SDK para utilização do PagSeguro em Python',
    url='https://pagseguro-sdk.readthedocs.com/',
    author='Jean O. Rodrigues',
    author_email='github@jean.bz',
    license='MIT',
    packages=['pagseguro'],
    install_requires=['requests>=2.4.0', 'beautifulsoup4>=4.3.0'],
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
