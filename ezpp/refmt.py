#!/usr/bin/env python3

import argparse
import re
import os
import shutil
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter, ImageColor
# readlines, writelines, readstr, readjson, list_by_ext
from ezutils.files import readjson

re_fmt = re.compile(r'^PNG|WEBP|JPG|JPEG$')

def brother_path(filename): return os.path.join(
    os.path.dirname(__file__), filename)


def create_cmd_parser(subparsers):
    parser_refmt = subparsers.add_parser(
        'refmt', help='Re format a picture',
    )
    parser_refmt.add_argument("-i",
                               "--infile",
                               help="The file to be refmt")
    parser_refmt.add_argument("-o",
                               "--outfile",
                               help="The output file refmt")
    refmt_group = parser_refmt.add_mutually_exclusive_group()
    refmt_group.add_argument("-f",
                              "--format",
                              help="File format. Like PNG, WEBP")

    parser_refmt.set_defaults(on_args_parsed=_on_args_parsed)


def _on_args_parsed(args):
    params = vars(args)
    infile = params['infile']
    outfile = params['outfile']
    fmt = params['format']
    _on_fmt_parsed(infile, outfile, fmt.upper())

def _on_fmt_parsed(infile, outfile, fmt):
    FMT = fmt.upper()
    m_fmt = re_fmt.match(FMT)
    if not m_fmt:
      return

    img = Image.open(os.path.abspath(infile))

    bar_filename, ext = os.path.splitext(infile)
    bar_filename_new,ext = outfile.splitext(infile) if outfile else (bar_filename, ext)
    ext = fmt.lower()
    filename_new = f"{bar_filename_new}.{ext}"

    print(f"comvert: {fmt}")
    print(f"from:   {os.path.abspath(infile)}")
    print(f"to:     {os.path.abspath(filename_new)}")

    out_dir, filename = os.path.split(filename_new)
    if len(out_dir) > 0 and not os.path.exists(out_dir):
        os.makedirs(out_dir)

    img.save(os.path.abspath(filename_new), FMT)

