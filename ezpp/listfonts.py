#!/usr/bin/env python3

# list fonts under system dirs and input dir

import os
from ezpp import global_args
from functools import reduce
from PIL import Image, ImageDraw, ImageFont
from ezpp.utils.fonts import get_sample_text
from imgcat import imgcat

import platform

platform_name = platform.system()
IS_MAC = platform_name == 'Darwin'
IS_WIN = platform_name == 'Windows'
IS_LINUX = platform_name == 'Linux'

if IS_WIN:
    USER_FONT_DIR = f'{os.environ["USERPROFILE"]}\AppData\Local\Microsoft\Windows\Fonts'
    SYS_FONT_DIR = 'C:\Windows\Fonts'
    TITLE_FONT = f'{SYS_FONT_DIR}\msyh.ttc'
elif IS_LINUX:
    USER_FONT_DIR = f'{os.environ["HOME"]}/.local/share/fonts'
    SYS_FONT_DIR = '/usr/share/fonts'
    TITLE_FONT = f'{SYS_FONT_DIR}/truetype/freefont/FreeMono.ttf'
elif IS_MAC:
    USER_FONT_DIR = f'{os.environ["HOME"]}/Library/Fonts'
    SYS_FONT_DIR = '/System/Library/Fonts'
    TITLE_FONT = f'{SYS_FONT_DIR}/Menlo.ttc'
else:
    USER_FONT_DIR = None
    SYS_FONT_DIR = None
    TITLE_FONT = None


def trim_font(font_path):
    path, filename = os.path.split(font_path)
    filename, ext = os.path.splitext(filename)
    return filename, font_path


def getsize(font, txt):
    """Get the size of the text."""
    bbox = font.getbbox(txt)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


def skip_font(fontname):
    skip_keywords = ['Emoji']
    for skip_keyword in skip_keywords:
        if fontname.find(skip_keyword) >= 0:
            return False

    skip_names = [
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
    print("font1:", fonts)

    fonts = list(filter(skip_font, fonts))
    print("font2:", fonts)
    fonts = list(map(trim_font, fonts))
    print("font3:", fonts)
    fonts.sort(key=lambda array: array[0])
    return fonts


def create_cmd_parser(subparsers):
    cmd_parser = subparsers.add_parser(
        'listfonts', help='listfonts help')
    cmd_parser.add_argument("-s",
                            "--system",
                            action='store_true',
                            help=f"list fonts in '{SYS_FONT_DIR}'")

    cmd_parser.add_argument("-u",
                            "--user",
                            action='store_true',
                            help=f"list fonts in '{USER_FONT_DIR}'")

    cmd_parser.add_argument("-i",
                            "--indir",
                            help="list fonts in indir")

    cmd_parser.add_argument("--index",
                            help="show detail of font by index of the font")

    cmd_parser.add_argument("-c",
                            "--imgcat",
                            action='store_true',
                            help="use imgcat show preview(for iterm2 only)")

    cmd_parser.set_defaults(on_args_parsed=_on_args_parsed)

    return cmd_parser


def _on_args_parsed(args):
    params = vars(args)

    user = params['user']
    index = params['index']
    imgcat = params['imgcat']

    if user:
        listfonts(f"{USER_FONT_DIR}", index, imgcat)

    system = params['system']
    if system:
        listfonts(f"{SYS_FONT_DIR}", index, imgcat)

    indir = params['indir']
    if indir:
        listfonts(indir, index, imgcat)


def is_imgcat_installed():
    filepath = f"{os.environ['HOME']}/.iterm2/imgcat"
    return os.path.isfile(filepath)


def list_max_line_length(fonts):
    return reduce(lambda last_len, current_line: last_len if last_len > len(current_line) else len(current_line), fonts, 0)


def listfonts(indir, index, imgcat):
    print('LIST:', indir)
    fonts = get_font_list(indir)
    count = len(fonts)
    max_number_width = len(f"{count}")

    titles = []
    if index is not None:
        index_value = int(index)
        fontname, fontpath = fonts[index_value]
        title = f"[{index_value:0{max_number_width}}/{count}] {fontname}"
        titles.append(title)
        if imgcat:
            print(title)
            imgcat_font(fonts[index_value])
        else:
            draw_fonts(titles,  [fonts[index_value]])
        return

    for i in range(0, count):
        fontname, fontpath = fonts[i]
        titles.append(f"[{i:0{max_number_width}}/{count}] {fontname}")

    if imgcat:
        imgcat_fonts(titles, fonts)
    else:
        draw_fonts(titles, fonts)


def draw_fonts(titles, fonts):
    LINE_HEIGHT = 20
    FONT_SIZE = 16

    TITLE_FONT_SIZE = 12
    MARGIN_SIZE = 4
    COLOR_BG = "#F93"
    COLOR_TEXT = "#543"

    count = len(fonts)
    max_number_width = len(f"{count}")
    x = MARGIN_SIZE
    y = MARGIN_SIZE

    h_total = 0
    w_max = 0
    titlefont = ImageFont.truetype(
        TITLE_FONT,
        TITLE_FONT_SIZE
    )

    for i in range(0, count):
        fontname, fontpath = fonts[i]
        demofont = ImageFont.truetype(fontpath, FONT_SIZE)
        text = get_sample_text(fontpath)
        title = titles[i]
        title_w, title_h = getsize(titlefont, title)
        w_max = max(w_max, title_w)
        demo_w, demo_h = getsize(demofont, text)
        w_max = max(w_max, demo_w)
        h_total = h_total + demo_h + title_h

    width = w_max + MARGIN_SIZE * 2
    height = MARGIN_SIZE * 2 + (MARGIN_SIZE * 3) * count + h_total
    img = Image.new('RGB', (width, height), COLOR_BG)
    draw = ImageDraw.Draw(img)

    for i in range(0, count):
        fontname, fontpath = fonts[i]
        title = titles[i]
        print(title)
        draw.line((0, y,  img.size[0], y), fill=128)
        y = y + MARGIN_SIZE

        draw.text((x, y), title, COLOR_TEXT, font=titlefont)
        title_w, title_h = getsize(titlefont, title)
        y = y + title_h + MARGIN_SIZE

        demofont = ImageFont.truetype(
            fontpath,
            FONT_SIZE
        )
        text = get_sample_text(fontpath)
        demo_w, demo_h = getsize(demofont, text)

        draw.text((x, y), text, COLOR_TEXT, font=demofont)
        y = y + demo_h + MARGIN_SIZE

    draw.line((0, y,  img.size[0], y), fill=128)
    img.show()


def imgcat_fonts(titles, fonts):
    count = len(fonts)
    max_number_width = len(f"{count}")

    for i in range(0, count):
        fontname, fontpath = fonts[i]
        print(f"[{i:0{max_number_width}}/{count}]:{fontpath}")
        imgcat_font(fonts[i])


def imgcat_font(font):
    LINE_HEIGHT = 20
    MARGIN_SIZE = 4
    COLOR_BG = "#F93"
    COLOR_TEXT = "#543"

    x = MARGIN_SIZE
    y = MARGIN_SIZE
    FONT_SIZE = 16
    fontname, fontpath = font
    demofont = ImageFont.truetype(
        fontpath,
        FONT_SIZE
    )
    text = get_sample_text(fontpath)
    demo_w, demo_h = getsize(demofont, text)
    width = demo_w + MARGIN_SIZE * 2
    height = demo_h + MARGIN_SIZE * 2

    img = Image.new('RGB', (width, height), COLOR_BG)
    draw = ImageDraw.Draw(img)
    draw.text((x, y), text, COLOR_TEXT, font=demofont)
    imgcat(img)


if __name__ == "__main__":
    listfonts('/System/Library/fonts')
