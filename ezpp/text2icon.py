#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter, ImageColor
import argparse
import os
import re
import colorsys
from . import global_args
from ezpp.utils.color_parser import *
from ezpp.utils.text import text_horzontal_center


ANTIALIAS_SIZE = 16
LOGO_SIZE = 1024*ANTIALIAS_SIZE
MAIN_POS_TITLE_ONLY = 512*ANTIALIAS_SIZE
MAIN_POS = 468*ANTIALIAS_SIZE
SUB_POS = 1000*ANTIALIAS_SIZE

# subtitle backgound副标题的背景
CIRCLE_RADIUS = 1380*ANTIALIAS_SIZE
CIRCLE_EDGE_Y = 848*ANTIALIAS_SIZE

DEFAULT_COLOR = '#ffffff'
DEFAULT_BGCOLOR = "#3399ff"
FONT_MAIN_SUM = 960*ANTIALIAS_SIZE
FONT_MAIN_SUM_MIN = 640*ANTIALIAS_SIZE
FONT_MAIN_SUM_STEP = 80*ANTIALIAS_SIZE
FONT_SIZE_SUB = 104*ANTIALIAS_SIZE


def brother_path(file_name):
    return os.path.join(os.path.abspath(
        os.path.dirname(__file__)), file_name)


def get_default_fontname():
    fonts = ['/System/Library/Fonts/PingFang.ttc',
             '/System/Library/Fonts/Menlo.ttc']
    for font in fonts:
        if os.path.isfile(font):
            return font
    return None


# brother_path('text2icon/ZhenyanGB.ttf')
DEFUALT_FONT_NAME = get_default_fontname()


def create_cmd_parser(subparsers):
    parser_recolor = subparsers.add_parser(
        'text2icon', help='Gen a 1024x1024 logo by text and color')
    parser_recolor.add_argument("-c",
                                "--color",
                                help=using_color)

    parser_recolor.add_argument("-b",
                                "--bgcolor",
                                help=using_color)

    parser_recolor.add_argument("-t",
                                "--title",
                                help="text of title")

    parser_recolor.add_argument("-s",
                                "--subtitle",
                                help="text of subtitle")

    parser_recolor.add_argument("-F",
                                "--font",
                                help="font of title")

    parser_recolor.add_argument("-f",
                                "--subfont",
                                help="font of subtitle")

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


def repeat2(str_tobe_repeat):
    if len(str_tobe_repeat) > 1:
        return str_tobe_repeat
    return str_tobe_repeat+str_tobe_repeat


def _on_args_parsed(args):
    params = vars(args)
    i, outfile, r, o, preview = global_args.parser_io_argments(params)
    text2icon(params, outfile, preview)


def font_path(font_name):
    return brother_path(font_name)


def text2icon(params, outfile, preview):

    title = params['title']
    subtitle = params['subtitle']
    font_name = params['font'] or DEFUALT_FONT_NAME
    subfont_name = params['subfont'] or DEFUALT_FONT_NAME
    color = params['color'] or DEFAULT_COLOR
    bgcolor = params['bgcolor'] or DEFAULT_BGCOLOR

    print(
        f'text2icon:\n[\n\ttitle:({title},font:{font_name}),\n\tsubtitle:({subtitle},subfont:{subfont_name}),\n\tcolor:{color},\n\tbgcolor:{bgcolor}\n]'
    )

    title_len = len(title)
    print('title_len', title, title_len)
    if title_len > 5:
        main_title_font_size = int(FONT_MAIN_SUM/title_len)
    else:
        main_title_font_size = int(
            (FONT_MAIN_SUM_MIN+(title_len-1)*FONT_MAIN_SUM_STEP)/1)

    main_title_font_size = FONT_MAIN_SUM_MIN if title_len == 1 else int(
        FONT_MAIN_SUM/title_len)
    font = ImageFont.load_default() if font_name is None else ImageFont.truetype(
        font_path(font_name),
        main_title_font_size
    )

    hasSubtitle = subtitle != None
    img = draw_bg(color, bgcolor, hasSubtitle)
    text_horzontal_center(
        title,
        color,
        font,
        img,
        LOGO_SIZE,
        (MAIN_POS if hasSubtitle else MAIN_POS_TITLE_ONLY) + main_title_font_size/2)

    font_sub = ImageFont.load_default() if subfont_name is None else ImageFont.truetype(
        font_path(subfont_name),
        FONT_SIZE_SUB
    )

    if hasSubtitle:
        text_horzontal_center(
            subtitle,
            bgcolor,
            font_sub,
            img,
            LOGO_SIZE,
            SUB_POS)

    logo_size = int(LOGO_SIZE/ANTIALIAS_SIZE)
    img = img.resize((logo_size, logo_size), Image.ANTIALIAS)

    if not outfile:
        new_outfile = f'{title}_{subtitle}.png' if subtitle else f'{title}.png'
    elif outfile[-1:] == "/":
        new_outfile = f"{outfile}{title}.png"
    else:
        new_outfile = outfile

    if preview:
        print("Preview Only")
        img.show()
    else:
        print("TO:", new_outfile)
        img.save(new_outfile)
