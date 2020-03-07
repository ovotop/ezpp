#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter, ImageColor
import argparse
import os
import re
import colorsys

using_color = "The color in hex value in formate of #RRGGBB  or #RGB. For example :#00ff00 or #0f0 make a  green version of your pic"

is_color_re = re.compile(r'^#?([0-9a-fA-f]{3}|[0-9a-fA-f]{6})$')
color3_re = re.compile(
    r'^#?([0-9a-fA-F]{1})([0-9a-fA-F]{1})([0-9a-fA-F]{1})$'
)
color6_re = re.compile(
    r'^#?([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})$'
)


def create_cmd_parser(subparsers):
    parser_recolor = subparsers.add_parser(
        'recolor', help='recolor a pic')
    parser_recolor.add_argument("--file",
                                "-f",
                                help="the file to be recolor")
    parser_recolor.add_argument("--color",
                                "-c",
                                help=using_color)
    # parser_recolor.add_argument("--outfile",
    #                             "-o",
    #                             help="Optional the output file")
    parser_recolor.set_defaults(on_args_parsed=_on_args_parsed)


def repeat2(str_tobe_repeat):
    if len(str_tobe_repeat) > 1:
        return str_tobe_repeat
    return str_tobe_repeat+str_tobe_repeat


def _on_args_parsed(args):
    params = vars(args)
    filename = params['file']
    color = params['color']

    if not is_color_re.match(color):
        print(using_color)
        exit(2)

    color_re = color6_re if len(color) > 4 else color3_re
    color_m = color_re.match(color)
    r = repeat2(color_m.group(1))
    g = repeat2(color_m.group(2))
    b = repeat2(color_m.group(3))
    recolor(filename, r, g, b)


def recolor(filename, red, green, blue):
    bar_filename, ext = os.path.splitext(filename)
    # src_h, src_s, src_v = colorsys.rgb_to_hsv(0, 152/255, 1)
    dst_h, dst_s, dst_v = colorsys.rgb_to_hsv(
        int(red, base=16)/255, int(green, base=16)/255, int(blue, base=16)/255)
    # print(dst_h, dst_s, dst_v)
    color = f"{red}{green}{blue}"
    new_filename = f"{bar_filename}_0x{color}{ext}"
    print(f"{filename} + #{color} -> {new_filename}")
    img = Image.open(filename).convert('RGBA')
    width = img.width
    height = img.height
    px = img.load()

    img_new = Image.new('RGBA', (width, height))
    px_new = img_new.load()

    for y in range(0, height):
        for x in range(0, width):
            r, g, b, a = px[x, y]
            h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
            rn, gn, bn = colorsys.hsv_to_rgb(dst_h, s, v)
            px_new[x, y] = (int(255*rn), int(255*gn), int(255*bn), a)

    img_new.save(new_filename, 'PNG')
