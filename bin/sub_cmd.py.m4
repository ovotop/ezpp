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
    infile, outfile, recursive, overwrite = global_args.parser_io_argments(params)

    yourArgumentStr = params['your_argument']
    if not yourArgumentStr:
        yourArgumentStr = 'defualt'

    __SUB_CMD__`'(infile, outfile, recursive, overwrite, yourArgumentStr)


def __SUB_CMD__`_'file(infile, outfile, overwrite, yourArgumentStr):
    new_filename = outfile
    if outfile == None:
        new_filename = global_args.auto_outfile(infile, "`_`__SUB_CMD__")


def __SUB_CMD__`'(infile, outfile, recursive,overwrite, sizeStr=10):

    if recursive == None or recursive == False:
        return __SUB_CMD__`_'file(infile, outfile, sizeStr)

    infiles = global_args.get_recursive_pic_infiles(infile)
    for infile_for_recursive in infiles:
        __SUB_CMD__`_'file(infile_for_recursive,
                           None,
                           sizeStr)
