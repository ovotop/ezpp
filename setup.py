#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: JeffreyCao
# Mail: jeffreycao1024@gmail.com
# Created Time:  2019-11-16 21:48:34
# https://packaging.python.org/guides/distributing-packages-using-setuptools/#package-data
#############################################

# from setuptools import setup, find_packages  # 这个包没有的可以pip一下
import setuptools

setuptools.setup(
    name="ezpp",
    version="0.0.2",
    keywords=("pip", "ezpp"),
    description="Tool to make zhike logos",
    long_description="Tool to make zhike logos",
    license="MIT Licence",

    url="https://github.com/caojianfeng/ezpp",
    author="JeffreyCao",
    author_email="jeffreycao1024@gmail.com",

    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={
        'ezpp': ['ZhenyanGB.ttf'],
    },
    platforms="any",
    install_requires=["Pillow"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'ezpp = ezpp.__main__:main'
        ]
    }
)
