#!/usr/bin/env python3
import os


def is_jpg(filename):
    fn, ext = os.path.splitext(filename)
    ext = ext.lower()
    return ext == '.jpg' or ext == '.jpeg'
