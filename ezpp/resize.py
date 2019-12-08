#!/usr/bin/env python3

import argparse
import re
import os

re_wh = re.compile(r'^([0-9]+)x([0-9]+)$')

size_using = """
The size shoud be [width]x[height] for example :300x400 . 
When width == heigth just use size number directly .
For example : 128 means a 128x128 size
"""


def create_cmd_parser(subparsers):
    parser_resize = subparsers.add_parser(
        'resize', help='resize a pic file',
    )
    parser_resize.add_argument("-f",
                               "--file",
                               help="The file to be resize")
    parser_resize.add_argument("-o",
                               "--outfile",
                               help="The output file resized")
    parser_resize.add_argument("-s",
                               "--size",
                               help=size_using)
    parser_resize.set_defaults(on_args_parsed=_on_args_parsed)


def _on_args_parsed(args):
    params = vars(args)
    filename = params['file']
    outfile = params['outfile']
    size = params['size']

    m_wh = re_wh.match(size)
    if not m_wh:
        print(size_using)
        exit(2)

    width = m_wh.group(1)
    height = m_wh.group(2)
    bar_filename, ext = os.path.splitext(filename)
    filename_new = outfile if outfile else f"{bar_filename}_{width}x{height}{ext}"
    resize(filename, width, height, filename_new)


def resize(filename, width, height, outputfile):
    print(f"{filename} -> {outputfile}")
