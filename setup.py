from guldlib import __version__
from setuptools import setup, find_packages

setup(name='guldlib',
      version=__version__,
      description='guld operations library',
      author='isysd',
      author_email='public@iramiller.com',
      license='MIT',
      url='https://guld.io/',
      py_modules = ['guldlib'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.4'
])
