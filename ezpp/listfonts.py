#!/usr/bin/env python3
# import argparse
# import os
# import re
from . import global_args

# list fonts under system dirs and input dir
# /System/Library/fonts
#
#


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
    infile, outfile, recursive, overwrite = global_args.parser_io_argments(
        params)

    yourArgumentStr = params['your_argument']
    if not yourArgumentStr:
        yourArgumentStr = 'defualt'

    listfonts(infile, outfile, recursive, overwrite, yourArgumentStr)


def listfonts_file(infile, outfile, overwrite, yourArgumentStr):
    new_filename = outfile
    if not outfile:
        new_filename = global_args.auto_outfile(infile, "_listfonts")
    print("listfonts")
    print('FROM:', infile)
    print('TO:', new_filename)


def listfonts(infile, outfile, recursive, overwrite, sizeStr=10):

    if recursive is None or not recursive:
        return listfonts_file(infile, outfile, sizeStr)

    infiles = global_args.get_recursive_pic_infiles(infile)
    for infile_for_recursive in infiles:
        listfonts_file(infile_for_recursive,
                       None,
                       sizeStr)
