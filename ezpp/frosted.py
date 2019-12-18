#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter
import argparse
import os
import re
from frosted_editer import frosted_editer

using_color = "The color in hex value in formate of #RRGGBB  or #RGB. For example :#00ff00 or #0f0 make a  green version of your pic"


def create_cmd_parser(subparsers):
    parser_recolor = subparsers.add_parser(
        'frosted', help='frosted glass on a pic')
    parser_recolor.add_argument("--file",
                                "-f",
                                help="the file to be frosted")
    parser_recolor.add_argument("--editer",
                                "-e",
                                action='store_true',
                                help="frosted pic in a editer window")
    parser_recolor.set_defaults(on_args_parsed=_on_args_parsed)


def repeat2(str_tobe_repeat):
    if len(str_tobe_repeat) > 1:
        return str_tobe_repeat
    return str_tobe_repeat+str_tobe_repeat


def _on_args_parsed(args):
    params = vars(args)
    filename = params['file']
    editer = params['editer']
    if editer:
        frosted_editer(filename)
    else:
        frosted(filename)


def frosted(filename):
    bar_filename, ext = os.path.splitext(filename)
    new_filename = f"{bar_filename}_frosted{ext}"
    print(f"{filename} frosted -> {new_filename}")
    img = Image.open(filename)
    img = img.filter(ImageFilter.GaussianBlur(10))
    img = img.filter(ImageFilter.ModeFilter(5))
    img.show()
    img.save(new_filename, 'PNG')
