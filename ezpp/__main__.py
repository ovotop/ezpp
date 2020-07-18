#!/usr/bin/env python3

import sys
import os
import getopt
import argparse
from . import global_args
from . import refmt
from . import frosted
from . import recolor
from . import resize
from . import text2icon
import sys

# https://docs.python.org/3/library/argparse.html#sub-commands


def add_global_argments(sub_parser):
    sub_parser.add_argument('-i',
                            '--infile',
                            help='the file to be recolor')
    sub_parser.add_argument('-r',
                            '--recursive',
                            action='store_true',
                            help='recursive the input file')
    sub_parser.add_argument('-o',
                            '--outfile',
                            help='Optional the output file')


def main():
    parser = argparse.ArgumentParser(
        prog="ezpp",
        usage="ezpp [-h] subcommand{recolor,resize} ...",
        description="Example: ezpp recolor -i my.png -c #00ff00"
    )

    subparsers = parser.add_subparsers(
        title='subcommands',
        dest='subcommands',
        description='ezpp [subcommand] [options]',
        help='subcommand using:ezpp [subcommand] -h')

    global_args.add_global_argments(frosted.create_cmd_parser(subparsers))
    global_args.add_global_argments(recolor.create_cmd_parser(subparsers))
    global_args.add_global_argments(resize.create_cmd_parser(subparsers))
    global_args.add_global_argments(refmt.create_cmd_parser(subparsers))
    global_args.add_global_argments(text2icon.create_cmd_parser(subparsers))

    if len(sys.argv) < 2:
        parser.print_help()
        exit(2)

    args = parser.parse_args()
    args.on_args_parsed(args)


if __name__ == "__main__":
    main()
