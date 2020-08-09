#!/usr/bin/env python3
from . import global_args
import re
import os
import argparse


def create_cmd_parser(subparsers):
    cmd_parser = subparsers.add_parser(
        'shadow', help='shadow help')
    cmd_parser.add_argument("-s",
                            "--size",
                            help="argument help")
    cmd_parser.set_defaults(on_args_parsed=_on_args_parsed)

    return cmd_parser


def _on_args_parsed(args):
    params = vars(args)
    infile, outfile, recursive = global_args.parser_io_argments(params)

    sizeStr = params['size']
    if not sizeStr:
        sizeStr = '10'

    shadow(infile, outfile, recursive, sizeStr)


def shadow_file(infile, outfile, blurSize):
    pass


def shadow(infile, outfile, recursive, sizeStr=10):

    if recursive == None or recursive == False:
        return shadow_file(infile, outfile, sizeStr)

    infiles = global_args.get_recursive_pic_infiles(infile)
    for infile_for_recursive in infiles:
        shadow_file(infile_for_recursive,
                    infile_for_recursive,
                    sizeStr)
