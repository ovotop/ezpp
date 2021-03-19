#!/usr/bin/env python3

import re
import os
from PIL import Image
from . import global_args
from ezpp.utils.filetype import is_jpg

re_fmt = re.compile(r'^PNG|WEBP|JPG|JPEG$')


def brother_path(filename): return os.path.join(
    os.path.dirname(__file__), filename)


def create_cmd_parser(subparsers):
    parser_refmt = subparsers.add_parser(
        'refmt', help='Re format a picture',
    )
    parser_refmt.add_argument("-f",
                              "--format",
                              help="File format. Like PNG, WEBP")

    parser_refmt.set_defaults(on_args_parsed=_on_args_parsed)

    return parser_refmt


def _on_args_parsed(args):
    params = vars(args)
    infile, outfile, recursive, o, p = global_args.parser_io_argments(params)
    fmt = params['format']
    on_fmt_parsed(infile, outfile, recursive, fmt.upper())


def is_same_fmt(fmt, ext):
    return fmt.lower() == ext[1:].lower()


def on_fmt_parsed(infile, outfile, recursive, fmt):
    if not recursive:
        return _on_fmt_parsed(infile, outfile, fmt)

    infiles = global_args.get_recursive_pic_infiles(infile)

    for infile_for_recursive in infiles:
        barfile, ext = os.path.splitext(infile_for_recursive)
        if is_same_fmt(fmt, ext):
            continue

        outfile = f'{barfile}{ext}'
        ok = _on_fmt_parsed(infile_for_recursive,
                            outfile, fmt)

        if ok:
            print(f'remove: {infile_for_recursive}')
            os.remove(infile_for_recursive)


def _on_fmt_parsed(infile, outfile, fmt):
    FMT = fmt.upper()
    m_fmt = re_fmt.match(FMT)
    if not m_fmt:
        return False

    with open(os.path.abspath(infile), 'rb') as imgfile:
        img = Image.open(imgfile)

        bar_filename, ext = os.path.splitext(infile)
        print(f"_on_fmt_parsed.ext:{ext}")
        bar_filename_new, ext = os.path.splitext(
            outfile) if outfile else (bar_filename, ext)
        ext = fmt.lower()
        filename_new = f"{bar_filename_new}.{ext}"

        print(f"comvert: {fmt}")
        print(f"from:   {os.path.abspath(infile)}")
        print(f"to:     {os.path.abspath(filename_new)}")

        out_dir, filename = os.path.split(filename_new)
        if len(out_dir) > 0 and not os.path.exists(out_dir):
            os.makedirs(out_dir)

        if is_jpg(filename):
            img = img.convert("RGB")

        img.save(os.path.abspath(filename_new), FMT)
    return True
