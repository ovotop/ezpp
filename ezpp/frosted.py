#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter
import argparse
import os
import re


def create_cmd_parser(subparsers):
    parser_recolor = subparsers.add_parser(
        'frosted', help='frosted glass on a pic')
    parser_recolor.add_argument("-i",
                                "--infile",
                                help="the file to be frosted")
    parser_recolor.add_argument("-s",
                                "--size",
                                help="size of frosted range, default 10, recommonded [3,20]")
    parser_recolor.set_defaults(on_args_parsed=_on_args_parsed)


def repeat2(str_tobe_repeat):
    if len(str_tobe_repeat) > 1:
        return str_tobe_repeat
    return str_tobe_repeat+str_tobe_repeat


def _on_args_parsed(args):
    params = vars(args)
    filename = params['infile']
    sizeStr = params['size']
    if not sizeStr:
        sizeStr = '10'

    size = int(sizeStr)
    mode = 5
    if size:
        if size > 5:
            mode = 5
        elif size > 3:
            mode = 3
        else:
            mode = 0

        frosted(filename, size, mode)
    else:
        frosted(filename)


def frosted(filename, blurSize=10, mode=5):
    bar_filename, ext = os.path.splitext(filename)
    new_filename = f"{bar_filename}_frosted{ext}"
    print(f"{filename} frosted(size = {blurSize}) -> {new_filename}")
    img = Image.open(filename)
    img = img.filter(ImageFilter.GaussianBlur(blurSize))

    if mode > 0:
        img = img.filter(ImageFilter.ModeFilter(mode))

    img.show()
    img.save(new_filename, 'PNG')
