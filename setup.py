# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="smime_dstu",
    version='0.1',
    url='https://github.com/muromec/smime-dstu',
    description='',
    author='Ilya Petrov',
    author_email='ilya.muromec@gmail.com',
    packages=["smime_dstu"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pyasn1',
    ],
    classifiers=[
        'Programming Language :: Python',
    ]
)
