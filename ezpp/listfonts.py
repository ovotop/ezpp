#!/usr/bin/env python3
# import argparse
# import re
import os
from . import global_args
# list fonts under system dirs and input dir
# /System/Library/fonts
#
#


def trim_font(font_path):
    path, filename = os.path.split(font_path)
    filename, ext = os.path.splitext(filename)
    return filename


def get_font_list(indir):
    font_exts = ['ttf', 'ttc', 'otf', 'dfont']
    fonts = global_args.get_recursive_infiles_by_ext(indir, font_exts)
    fonts = list(map(trim_font, fonts))
    fonts.sort()
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


def listfonts(indir):
    print("listfonts")
    print('iterm2.imgcat:', is_imgcat_installed())
    print('LIST:', indir)
    fonts = get_font_list(indir)
    count = len(fonts)
    max_width = len(f"{count}")
    for i in range(0, count):
        font = fonts[i]
        print(f"[{i:0{max_width}}/{count}]{font}")
