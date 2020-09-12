#!/usr/bin/env python3

import re
import os
import shutil
from PIL import Image
# readlines, writelines, readstr, readjson, list_by_ext
from ezutils.files import readjson
from . import global_args

re_wh = re.compile(r'^([0-9]+)x([0-9]+)$')
re_size = re.compile(r'^([0-9]+)$')
re_percent = re.compile(r'^([0-9|.]+)%$')

size_using = """
(1) WIDTH AND HEIGHT For example :300x400 ;
(2) SIZE OF SQUARE For example : 128 means a 128x128 size ;
(3) PERCENT For example : 25%% ;
"""


def brother_path(filename): return os.path.join(
    os.path.dirname(__file__), filename)


def create_cmd_parser(subparsers):
    parser_resize = subparsers.add_parser(
        'resize', help='resize a pic',
    )
    resize_group = parser_resize.add_mutually_exclusive_group()
    resize_group.add_argument("-s",
                              "--size",
                              help=size_using)
    resize_group.add_argument("-a",
                              "--app",
                              action='store_true',
                              help="Resize app icons for android and ios")

    parser_resize.set_defaults(on_args_parsed=_on_args_parsed)

    return parser_resize


def _on_args_parsed(args):
    params = vars(args)
    app = params['app']
    infile, outfile, recursive, o, p = global_args.parser_io_argments(params)
    size = params['size']

    if app:
        _on_app_parsed(infile, outfile)
    else:
        on_size_parsed(infile, outfile, recursive, size)


def _on_app_parsed(infile, outfile):
    with open(os.path.abspath(infile), 'rb') as imgfile:
        img = Image.open(imgfile)
        (origin_w, origin_h) = img.size
        if origin_h != 1024 or origin_w != 1024:
            print("Input file should be 1024x1024 picture !")
            return

        cfg_dir = brother_path('resize_cfg')
        cfg_file = f"{cfg_dir}/app_icon.json"
        resize_cfgs, copy_cfgs = _get_icon_sizes_from_cfg(cfg_file)

        output_dir = outfile or f"{infile}.out"

        index = 0
        count = len(resize_cfgs)
        for cfg in resize_cfgs:
            filename = cfg.get("filename")
            size = cfg.get("size")
            print(f"[{index+1}/{count}]--------- RESIZE ----------")
            _resize(infile, f"{output_dir}/{filename}", origin_w, origin_h,
                    size, size, img)
            index += 1

        index = 0
        count = len(copy_cfgs)
        for cfg in copy_cfgs:
            print(f"[{index+1}/{count}]--------- COPY ----------")
            _copy(os.path.abspath(f"{cfg_dir}/{cfg.get('from')}"),
                  os.path.abspath(f"{output_dir}/{cfg.get('to')}"))
            index += 1


def _get_icon_sizes_from_cfg(cfg_file):
    cfgs = readjson(cfg_file)
    # print(cfgs)

    icons_cfg = cfgs['icons']
    copies_cfg = cfgs['copies']
    return icons_cfg, copies_cfg


def on_size_parsed(infile, outfile, recursive, size):
    print(f"on_size_parsed({infile}, {outfile}, {recursive}, {size})")
    if not recursive:
        return _on_size_parsed(infile, outfile, size)

    infiles = global_args.get_recursive_pic_infiles(infile)
    for infile_for_recursive in infiles:
        _on_size_parsed(infile_for_recursive,
                        None,
                        size)


def _on_size_parsed(infile, outfile, size):
    with open(os.path.abspath(infile), 'rb') as imgfile:
        img = Image.open(imgfile)
        (origin_w, origin_h) = img.size

        (width, height) = _parse_wh_from_size(size, origin_w, origin_h)
        new_width = width
        new_height = height

        if width < 1 and height < 1:

            new_width = int(origin_w * width)
            new_height = int(origin_h * height)

        newFile = outfile
        if outfile is None or outfile is None:
            newFile = global_args.auto_outfile(
                infile, f"_{new_width}x{new_height}")

        _resize(infile, newFile, origin_w, origin_h,
                new_width, new_height, img)


def _resize(infile, outfile, origin_w, origin_h, new_width, new_height, img):
    print(f"resize: ({origin_w}, {origin_h})->({new_width}, {new_height})")
    print(f"from:   {os.path.abspath(infile)}")
    print(f"to:     {os.path.abspath(outfile)}")

    out_dir, filename = os.path.split(outfile)
    if len(out_dir) > 0 and not os.path.exists(out_dir):
        os.makedirs(out_dir)

    img_tobe_scale = img.resize(
        (int(new_width), int(new_height)), Image.ANTIALIAS)
    img_tobe_scale.save(os.path.abspath(outfile), 'PNG')


def _copy(src_file, dst_file):
    print(f"from:    {src_file}")
    print(f"copy to: {dst_file}")
    out_dir, filename = os.path.split(dst_file)
    if len(out_dir) > 0 and not os.path.exists(out_dir):
        os.makedirs(out_dir)
    shutil.copy(src_file, dst_file)


def _parse_wh_from_size(size, origin_w, origin_h):
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
        ratio = float(m_percent.group(1))/float(100)
        return (int(origin_w*ratio), int(origin_h*ratio))
    else:
        print(size_using)
        exit(2)
