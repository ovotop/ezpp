#!/usr/bin/env python3

import argparse
import re
import os
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter, ImageColor

re_wh = re.compile(r'^([0-9]+)x([0-9]+)$')
re_size = re.compile(r'^([0-9]+)$')
re_percent = re.compile(r'^([0-9]+)%$')

size_using = """
(1) WIDTH AND HEIGHT For example :300x400 ;
(2) SIZE OF SQUARE For example : 128 means a 128x128 size ;
(3) PERCENT For example : 25%% ;
"""


def create_cmd_parser(subparsers):
    parser_resize = subparsers.add_parser(
        'resize', help='resize a pic',
    )
    parser_resize.add_argument("-f",
                               "--file",
                               help="The file to be resize")
    parser_resize.add_argument("-o",
                               "--outfile",
                               help="The output file resized")
    resize_group = parser_resize.add_mutually_exclusive_group()
    resize_group.add_argument("-s",
                              "--size",
                              help=size_using)
    resize_group.add_argument("-a",
                              "--app",
                              action='store_true',
                              help="Resize app icons for android and ios")

    parser_resize.set_defaults(on_args_parsed=_on_args_parsed)


def _on_args_parsed(args):
    params = vars(args)
    app = params['app']
    infile = params['file']
    outfile = params['outfile']
    size = params['size']

    if app:
        _on_app_parsed(infile, outfile)
    else:
        _on_size_parsed(infile, outfile, size)


def _on_app_parsed(infile, outfile):
    new_width = 192
    new_height = 192
    img = Image.open(os.path.abspath(infile))
    (origin_w, origin_h) = img.size
    if origin_h != 1024 or origin_w != 1024:
        print("Input file should be 1024x1024 picture !")
        return

    _resize(infile, outfile, origin_w, origin_h, new_width, new_height, img)


def _on_size_parsed(infile, outfile, size):

    (width, height) = _parse_wh_from_size(size)
    new_width = width
    new_height = height

    img = Image.open(os.path.abspath(infile))
    (origin_w, origin_h) = img.size

    if width < 1 and height < 1:

        new_width = int(origin_w * width)
        new_height = int(origin_h * height)

    _resize(infile, outfile, origin_w, origin_h, new_width, new_height, img)


def _resize(infile, outfile, origin_w, origin_h, new_width, new_height, img):
    bar_filename, ext = os.path.splitext(infile)
    filename_new = outfile if outfile else f"{bar_filename}_{new_width}x{new_height}{ext}"

    print(f"resize: ({origin_w}, {origin_h})->({new_width}, {new_height})")
    print(f"from:   {os.path.abspath(infile)}")
    print(f"to:     {os.path.abspath(filename_new)}")

    img_tobe_scale = img.resize(
        (int(new_width), int(new_height)), Image.ANTIALIAS)
    img_tobe_scale.save(os.path.abspath(filename_new), 'PNG')


def _parse_wh_from_size(size):
    m_wh = re_wh.match(size)
    if m_wh:
        width = int(m_wh.group(1))
        height = int(m_wh.group(2))
        return (width, height)

    m_size = re_size.match(size)
    if m_size:
        width = int(m_size.group(1))
        height = width
        return (width, height)

    m_percent = re_percent.match(size)
    if m_percent:
        width = float(m_percent.group(1))/float(100)
        height = width
        return (width, height)
    else:
        print(size_using)
        exit(2)
