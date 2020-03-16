#!/usr/bin/env python3

import sys
import os
import getopt
import argparse
from . import refmt
from . import frosted
from . import recolor
from . import resize
import sys

# https://docs.python.org/3/library/argparse.html#sub-commands


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
    
    frosted.create_cmd_parser(subparsers)
    recolor.create_cmd_parser(subparsers)
    resize.create_cmd_parser(subparsers)
    refmt.create_cmd_parser(subparsers)

    if len(sys.argv) < 2:
        parser.print_help()
        exit(2)

    args = parser.parse_args()
    args.on_args_parsed(args)


if __name__ == "__main__":
    main()
