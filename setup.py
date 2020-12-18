#!/usr/bin/env python

import os
import sys
from shutil import rmtree
from setuptools import setup, find_namespace_packages

pkgname = 'woeplanet.utils.uri'
cwd = os.path.dirname(os.path.realpath(sys.argv[0]))
egginfo = '%s/%s.egg_info' % (cwd, pkgname)
if os.path.exists(egginfo):
    rmtree(egginfo)

version = open('VERSION').read()
nspkgs = find_namespace_packages(include=['woeplanet.utils.*'])

setup(
    name=pkgname,
    python_requires='>3',
    packages=nspkgs,
    version=version,
    description='Tools for working with URIs for WoePlanet documents',
    author='Gary Gale',
    url='https://github.com/woeplanet/py-woeplanet-uri',
    download_url='https://github.com/woeplanet/py-woeplanet-uri/releases/tag/' + version,
    license='BSD-3-Clause'
)
