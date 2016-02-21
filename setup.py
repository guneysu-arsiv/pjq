# coding: utf-8
import io
import re
from setuptools import setup

init_py = io.open('pjq/__init__.py').read()
metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", init_py))
metadata['doc'] = re.findall('"""(.+)"""', init_py)[0]

setup(
    name='pjq',
    version=metadata['version'],
    description=metadata['doc'],
    author=metadata['author'],
    author_email=metadata['email'],
    url=metadata['url'],
    packages=['pjq', 'pjq.syntax', 'tests'],
    install_requires=io.open('requirements.txt').readlines(),
    scripts=['bin/pjq'],
    license=open('LICENSE').read(),
)
