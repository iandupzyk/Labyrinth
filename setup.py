#!/usr/bin/env python

from distutils.core import setup

setup(name='Labyrinth',
      version='0.1.0',
      description='Multi-Node Job Scheduler',
      author='Ian Dupzyk',
      author_email='ian.dupzyk@gmail.com',
      url='',
      packages=['Labyrinth'],
      install_requires=[
          'flask',
          'flask_restful',
          'json',
          'logging',
          'os'
          ]
     )
