#!/usr/bin/env python3

import sys
import os
import getopt
import argparse

# SUB COMMONDS DEF[
# https://docs.python.org/3/library/argparse.html#sub-commands
from . import global_args
from . import refmt
from . import frosted
from . import recolor
from . import resize
from . import text2icon
from . import shadow
# IMPORT SUBCMD DEF HERE
# SUB COMMONDS DEF]


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

    # SUB COMMONDS ARGMENTS[
    global_args.add_global_argments(frosted.create_cmd_parser(subparsers))
    global_args.add_global_argments(recolor.create_cmd_parser(subparsers))
    global_args.add_global_argments(resize.create_cmd_parser(subparsers))
    global_args.add_global_argments(refmt.create_cmd_parser(subparsers))
    global_args.add_global_argments(text2icon.create_cmd_parser(subparsers))
    global_args.add_global_argments(shadow.create_cmd_parser(subparsers))
    # ADD SUBCMD ARGMENTS HERE
    # SUB COMMONDS ARGMENTS]

    if len(sys.argv) < 2:
        parser.print_help()
        exit(2)

    args = parser.parse_args()
    args.on_args_parsed(args)


if __name__ == "__main__":
    main()
