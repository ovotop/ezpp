#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter, ImageColor
import argparse
import os
import re
import colorsys
from . import global_args
from ezpp.utils.color_parser import *
# using_color = "-c The color in hex value in formate of #RRGGBB  or #RGB. For example :#00ff00 or #0f0 make a  green version of your pic"
# is_color_re = re.compile(r'^#?([0-9a-fA-f]{3}|[0-9a-fA-f]{6})$')
# color3_re = re.compile(
#     r'^#?([0-9a-fA-F]{1})([0-9a-fA-F]{1})([0-9a-fA-F]{1})$'
# )
# color6_re = re.compile(
#     r'^#?([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})$'
# )

# https://www.zcool.com.cn/article/ZNDg2Mzg4.html
# FONT_FILE_NAME = 'HappyZcool-2016.ttf'
# FONT_FILE_NAME = 'zcoolqinkehuangyouti.ttf'
# FONT_FILE_NAME = 'lianmengqiyilushuaizhengruiheiti.ttf'

FONT_FILE_NAME = 'text2icon/ZhenyanGB.ttf'
ANTIALIAS_SIZE = 16
LOGO_SIZE = 1024*ANTIALIAS_SIZE
MAIN_POS_TITLE_ONLY = 512*ANTIALIAS_SIZE
MAIN_POS = 468*ANTIALIAS_SIZE
SUB_POS = 1000*ANTIALIAS_SIZE
# 副标题的背景
CIRCLE_RADIUS = 1380*ANTIALIAS_SIZE
CIRCLE_EDGE_Y = 848*ANTIALIAS_SIZE
DEFAULT_COLOR = '#ffffff'
DEFAULT_BGCOLOR = "#3399ff"
FONT_MAIN_SUM = 840*ANTIALIAS_SIZE
FONT_SIZE_SUB = 104*ANTIALIAS_SIZE


def brother_path(file_name):
    return os.path.join(os.path.abspath(
        os.path.dirname(__file__)), file_name)


def create_cmd_parser(subparsers):
    parser_recolor = subparsers.add_parser(
        'text2icon', help='Gen a 1024x1024 logo by text and color')
    parser_recolor.add_argument("--color",
                                "-c",
                                help=using_color)

    parser_recolor.add_argument("--bgcolor",
                                "-b",
                                help=using_color)

    parser_recolor.add_argument("--title",
                                "-t",
                                help=using_color)

    parser_recolor.add_argument("--subtitle",
                                "-s",
                                help=using_color)

    parser_recolor.set_defaults(on_args_parsed=_on_args_parsed)

    return parser_recolor


def draw_bg(color, bgcolor, hasSubtitle):
    img = Image.new('RGB', (LOGO_SIZE, LOGO_SIZE), bgcolor)
    draw = ImageDraw.Draw(img)
    if hasSubtitle:
        ellipseX1 = LOGO_SIZE/2 - CIRCLE_RADIUS
        ellipseX2 = LOGO_SIZE/2 + CIRCLE_RADIUS
        draw.ellipse((ellipseX1, CIRCLE_EDGE_Y, ellipseX2,
                      CIRCLE_EDGE_Y+CIRCLE_RADIUS*2), color)
    return img


def text_horzontal_center(text, color, font, img, base_y):
    text_width, text_height = font.getsize(text)
    draw = ImageDraw.Draw(img)
    x = (LOGO_SIZE-text_width)/2
    y = base_y-text_height
    draw.text((x, y), text, color, font=font)


def repeat2(str_tobe_repeat):
    if len(str_tobe_repeat) > 1:
        return str_tobe_repeat
    return str_tobe_repeat+str_tobe_repeat


def _on_args_parsed(args):
    params = vars(args)
    i, outfile, r, o = global_args.parser_io_argments(params)
    text2icon(params, outfile)


def text2icon(params, outfile):

    title = params['title']
    subtitle = params['subtitle']
    color = params['color'] or DEFAULT_COLOR
    bgcolor = params['bgcolor'] or DEFAULT_BGCOLOR

    print(
        f'text2icon:[title:{title},subtitle:{subtitle},color:{color},bgcolor:{bgcolor}]'
    )

    title_len = len(title)
    main_title_font_size = int(FONT_MAIN_SUM/title_len)
    font = ImageFont.truetype(
        brother_path(FONT_FILE_NAME),
        main_title_font_size
    )
    hasSubtitle = subtitle != None
    img = draw_bg(color, bgcolor, hasSubtitle)
    text_horzontal_center(
        title,
        color,
        font,
        img,
        (MAIN_POS if hasSubtitle else MAIN_POS_TITLE_ONLY) + main_title_font_size/2)

    font_sub = ImageFont.truetype(
        brother_path(FONT_FILE_NAME),
        FONT_SIZE_SUB
    )

    if hasSubtitle:
        text_horzontal_center(
            subtitle,
            bgcolor,
            font_sub,
            img,
            SUB_POS)

    logo_size = int(LOGO_SIZE/ANTIALIAS_SIZE)
    img = img.resize((logo_size, logo_size), Image.ANTIALIAS)
    new_outfile = outfile if outfile else f'{title}_{subtitle}.png' if subtitle else f'{title}.png'
    img.save(new_outfile, 'PNG')
