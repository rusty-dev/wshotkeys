#!/usr/bin/python3

from setuptools import setup

setup(
    name='wshotkeys',
    version='2.0',
    author='https://github.com/rusty-dev',
    author_email='rustykoc@gmail.com',
    url='https://github.com/rusty-dev/wshotkeys',
    install_requires=['click', 'keyboard', 'websockets'],
    scripts=['wshotkeys'],
)
