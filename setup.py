#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='etcd3autodiscover',
    description='Wrapper around python-etcd3 to support DNS SRV discovery of endpoints',
    url='git@github.com:sysoperator/python-etcd3autodiscover.git',
    author='Piotr Mazurkiewicz',
    author_email='piotr.mazurkiewicz@sysoperator.pl',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7'
    ],
    keywords='',
    package_dir={'': 'src'},
    packages=['etcd3autodiscover'],
    install_requires=[
        'dnspython',
        'tornado>=4.5.0',
        'etcd3',
    ],
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
)

