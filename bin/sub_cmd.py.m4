#!/usr/bin/env python3
import argparse
import os
import re
from . import global_args

def create_cmd_parser(subparsers):
    cmd_parser = subparsers.add_parser(
        '__SUB_CMD__', help='__SUB_CMD__ help')
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

    __SUB_CMD__`'(infile, outfile, recursive, sizeStr)


def __SUB_CMD__`_'file(infile, outfile, blurSize):
    pass


def __SUB_CMD__`'(infile, outfile, recursive, sizeStr=10):

    if recursive == None or recursive == False:
        return __SUB_CMD__`_'file(infile, outfile, sizeStr)

    infiles = global_args.get_recursive_pic_infiles(infile)
    for infile_for_recursive in infiles:
        __SUB_CMD__`_'file(infile_for_recursive,
                           infile_for_recursive,
                           sizeStr)
