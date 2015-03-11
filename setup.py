#! /usr/bin/env python
# encoding: utf-8

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

__version__ = '0.1.2'

setup(
    name='pagseguro-sdk',
    version=__version__,
    description='SDK para utilização do PagSeguro em Python',
    url='http://github.com/jeanmask/pagseguro-sdk/',
    author='Jean O. Rodrigues',
    author_email='github@jean.bz',
    download_url='https://github.com/jeanmask/pagseguro-sdk/archive/v{0}.tar.gz'.format(__version__),
    license='MIT',
    packages=find_packages(exclude=('doc', 'docs', 'example')),
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
    keywords=['pagseguro', 'sdk', 'python']
)
