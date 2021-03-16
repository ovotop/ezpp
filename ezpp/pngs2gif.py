#!/usr/bin/env python3
# import argparse
import os
# import re
from . import global_args
from PIL import Image, ImageSequence


def create_cmd_parser(subparsers):
    cmd_parser = subparsers.add_parser(
        'pngs2gif', help='input dir files: [index]_[duration by ms]_***.png')
    cmd_parser.add_argument("-d",
                            "--duration",
                            help="default duration covered by "
                            "duration in filename")
    cmd_parser.set_defaults(on_args_parsed=_on_args_parsed)

    return cmd_parser


def _on_args_parsed(args):
    params = vars(args)
    infile, outfile, r, overwrite, preview = global_args.parser_io_argments(
        params)

    print(f'args: {infile}, {outfile}, {r}, {overwrite}, {preview} ')
    duration = params['duration']
    if not duration:
        duration = '1'

    if outfile is None:
        outfile = f"{infile}.gif"

    pngs2gif(infile, outfile, overwrite, preview, duration)


def pngs2gif_file(infiles, outfile, overwrite, preview, duration):
    print("===== pngs2gif =====")
    print('FROM:', infiles)
    print('preview:', preview)
    print('TO:', outfile)
    print('duration:', duration)

    images = []
    durations = []
    for infile in infiles:
        images.append(Image.open(infile))
        durations.append(int(duration))

    images[0].save(outfile,
                   format="GIF",
                   save_all=True,
                   append_images=images[1:],
                   duration=durations,
                   disposal=2,
                   background=1,
                   loop=0,
                   optimize=False,
                   transparency=0)
    index = 0
    for frame in images:
        frame.save(f"frame{index}.png")
        index += 1

    print("----- pngs2gif -----")


def pngs2gif(infile, outfile, overwrite, preview, duration=1):

    infiles = global_args.get_recursive_pic_infiles(infile)
    infiles.sort()
    pngs2gif_file(infiles,
                  outfile,
                  overwrite,
                  preview,
                  duration)
