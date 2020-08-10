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
    version="0.1.5",
    keywords=["pip", "ezpp", "resize", "reformat", "recolor", "shadow"],
    description="Easy to process picturse",
    long_description="Easy to process picturse",
    license="MIT Licence",

    url="https://github.com/ovotop/ezpp",
    author="JeffreyCao",
    author_email="jeffreycao1024@gmail.com",

    packages=setuptools.find_packages(exclude=['docs', 'playground', 'bin']),
    include_package_data=True,
    package_data={
        'ezpp': ['text2icon/ZhenyanGB.ttf', 'resize_cfg/app_icon.json', 'resize_cfg/Contents.json'],
    },
    platforms="any",
    install_requires=["Pillow", "ezutils"],
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
