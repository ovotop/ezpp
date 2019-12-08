#!/usr/bin/env python3

import sys
import os
import getopt
import argparse
import recolor
import resize
import frosted


# https://docs.python.org/3/library/argparse.html#sub-commands
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="ezpp",
        usage="ezpp [-h] subcommand{recolor,resize} ...",
        description="Example: ezpp recolor -f my.png -c #00ff00"
    )
    subparsers = parser.add_subparsers(
        title='subcommands',
        dest='subcommands',
        description='ezpp [subcommand] [options]',
        help='subcommand using:ezpp [subcommand] -h')
    frosted.create_cmd_parser(subparsers)
    recolor.create_cmd_parser(subparsers)
    resize.create_cmd_parser(subparsers)
    args = parser.parse_args()
    args.on_args_parsed(args)
