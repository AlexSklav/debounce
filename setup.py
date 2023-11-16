#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages

import versioneer

# See https://blog.ionelmc.ro/2014/06/25/python-packaging-pitfalls/
setup(name='debounce',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='Python port of lodash.debounce',
      keywords='',
      author='Christian Fobel',
      author_email='christian@fobel.net',
      url='https://github.com/sci-bots/debounce',
      license='BSD',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      py_modules=['debounce'],
      # Install data listed in `MANIFEST.in`
      include_package_data=True)
