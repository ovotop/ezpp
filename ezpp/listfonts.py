#!/usr/bin/env python3
# import argparse
# import re
import os
from ezpp import global_args
from functools import reduce
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter, ImageColor
# list fonts under system dirs and input dir
# /System/Library/fonts
#
#


def trim_font(font_path):
    path, filename = os.path.split(font_path)
    filename, ext = os.path.splitext(filename)
    return filename, font_path


def skip_font(fontname):
    skip_keywords = ['Braille', 'Emoji']
    for skip_keyword in skip_keywords:
        if fontname.find(skip_keyword) >= 0:
            return False

    skip_names = [
        '/System/Library/fonts/Symbol.ttf',  # 数学公式
        '/System/Library/fonts/ZapfDingbats.ttf',  # 图标字体
        '/System/Library/fonts/Supplemental/NISC18030.ttf',  # 股票字体
    ]
    for skip_name in skip_names:
        if fontname == skip_name:
            return False
    # print('keep fontname:', fontname)
    return True


def get_font_list(indir):
    font_exts = ['ttf', 'ttc', 'otf', 'dfont']

    fonts = global_args.get_recursive_infiles_by_ext(indir, font_exts)
    fonts = list(filter(skip_font, fonts))[0:10]
    fonts = list(map(trim_font, fonts))
    fonts.sort(key=lambda array: array[0])
    return fonts


def create_cmd_parser(subparsers):
    cmd_parser = subparsers.add_parser(
        'listfonts', help='listfonts help')
    cmd_parser.add_argument("-s",
                            "--system",
                            action='store_true',
                            help="list fonts in '/System/Library/fonts'")
    cmd_parser.add_argument("-u",
                            "--user",
                            action='store_true',
                            help="list fonts in '~/Library/Fonts'"
                            " and '/Library/Fonts'")
    cmd_parser.add_argument("-i",
                            "--indir",
                            help="list fonts in indir")
    cmd_parser.set_defaults(on_args_parsed=_on_args_parsed)

    return cmd_parser


def _on_args_parsed(args):
    params = vars(args)

    user = params['user']
    if user:
        listfonts(f"{os.environ['HOME']}/Library/fonts")
        listfonts('/Library/fonts')

    system = params['system']
    if system:
        listfonts('/System/Library/fonts')

    indir = params['indir']
    if indir:
        listfonts(indir)


def is_imgcat_installed():
    filepath = f"{os.environ['HOME']}/.iterm2/imgcat"
    return os.path.isfile(filepath)


def list_max_line_length(fonts):
    return reduce(lambda last_len, current_line: last_len if last_len > len(current_line) else len(current_line), fonts, 0)


def listfonts(indir):
    print("listfonts")
    print('iterm2.imgcat:', is_imgcat_installed())
    print('LIST:', indir)
    fonts = get_font_list(indir)
    count = len(fonts)
    max_number_width = len(f"{count}")

    titles = []
    for i in range(0, count):
        fontname, fontpath = fonts[i]
        titles.append(f"[{i:0{max_number_width}}/{count}] {fontname}")

    draw_fonts(titles, fonts)


def draw_fonts(titles, fonts):
    LINE_HEIGHT = 20
    FONT_SIZE = 16
    TITLE_FONT = '/System/Library/fonts/Menlo.ttc'
    TITLE_FONT_SIZE = 12
    MARGIN_SIZE = 4
    COLOR_BG = "#F93"
    COLOR_TEXT = "#543"

    max_title_len = list_max_line_length(titles)
    print('max_title_len', max_title_len)

    count = len(fonts)

    width = max_title_len * FONT_SIZE
    height = (LINE_HEIGHT + MARGIN_SIZE) * count

    print("width:", width)
    print("height:", height)

    img = Image.new('RGB', (width, height), COLOR_BG)
    draw = ImageDraw.Draw(img)
    x = MARGIN_SIZE
    y = MARGIN_SIZE
    for i in range(0, count):
        fontname, fontpath = fonts[i]
        demofont = ImageFont.truetype(fontpath, FONT_SIZE)
        text = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        demosize = demofont.getsize(text)

    for i in range(0, count):
        fontname, fontpath = fonts[i]
        title = titles[i]

        # print("fontpath:", fontpath)
        # print("FONT_SIZE:", FONT_SIZE)

        titlefont = ImageFont.truetype(
            TITLE_FONT,
            TITLE_FONT_SIZE
        )

        y = y + (LINE_HEIGHT + MARGIN_SIZE)
        draw.line((0, y,  img.size[0], y), fill=128)
        y = y + MARGIN_SIZE
        draw.text((x, y), title, COLOR_TEXT, font=titlefont)

        demofont = ImageFont.truetype(
            fontpath,
            FONT_SIZE
        )
        text = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        demosize = demofont.getsize(text)
        y = y + demosize[1]
        draw.text((x, y), text, COLOR_TEXT, font=demofont)

    img.show()


if __name__ == "__main__":
    listfonts('/System/Library/fonts')
