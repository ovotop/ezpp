#!/usr/bin/env python3
import argparse
import os
import re
from . import global_args

def create_cmd_parser(subparsers):
    cmd_parser = subparsers.add_parser(
        'layout', help='layout help')
    cmd_parser.add_argument("-p",
                            "--params",
                            help='params map,like \"{w:960,h:540,title:"hello"}\"')
    cmd_parser.set_defaults(on_args_parsed=_on_args_parsed)

    return cmd_parser


def _on_args_parsed(args):
    params = vars(args)
    infile, outfile, r, o = global_args.parser_io_argments(params,recursive = false,overwrite = false)

    params = params['params']
    if not params:
        params = '{}'

    layout(infile, outfile, params)


def layout(infile, outfile,sizeStr=10):
    pass

