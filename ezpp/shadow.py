#!/usr/bin/env python3
import os
import re
import sys
import argparse
from PIL import Image, ImageColor
from ezutils.colors import *
from . import global_args

COLOR_SAME_RADUS = 160


def create_cmd_parser(subparsers):
    cmd_parser = subparsers.add_parser(
        'shadow', help='Add long shadow on a image which has clean background')
    cmd_parser.add_argument("-a",
                            "--alpha",
                            help="(0.0,1.0] 0.0 None shadow 1.0 black shadow")
    cmd_parser.set_defaults(on_args_parsed=_on_args_parsed)

    return cmd_parser


def _on_args_parsed(args):
    params = vars(args)
    infile, outfile, recursive, overwrite = global_args.parser_io_argments(
        params)

    alphaStr = params['alpha']
    if not alphaStr:
        alphaStr = '0.5'
    alpha = float(alphaStr)
    shadow(infile, outfile, recursive, overwrite, alpha)


def sameColor(colorA, colorB):
    r = colorA[0] - colorB[0]
    g = colorA[1] - colorB[1]
    b = colorA[2] - colorB[2]
    return r*r+g*g+b*b < COLOR_SAME_RADUS*COLOR_SAME_RADUS


def shadowColor(colorbg, alpha):
    r, g, b = colorbg
    h, s, v = rgb2hsv(r, g, b)
    r1, g1, b1 = hsv2rgb(h, s, (1-alpha)*v)
    strHex = bytearray([r1, g1, b1]).hex()
    return f"#{strHex}"


def shadowOnline(pixes, width, height, fromX, fromY, alpha):
    first = None
    firstObj = None
    for i in range(0, width):
        x = fromX+i
        y = fromY+i
        if x >= width or y >= height:
            continue

        if first == None:
            first = pixes[x, y]
            continue

        if firstObj == None:
            if not sameColor(first, pixes[x, y]):
                firstObj = pixes[x, y]
            continue

        if sameColor(first, pixes[x, y]):
            pixes[x, y] = ImageColor.getcolor(
                shadowColor(pixes[x, y], alpha), "RGB")


def shadowOnPixes(pixes, width, height, alpha):
    for i in range(0, width):
        shadowOnline(pixes, width, height, i, 0, alpha)

    for j in range(1, height):
        shadowOnline(pixes, width, height, 0, j, alpha)


def shadowOnImage(img, alpha):
    imgSize = img.size
    pixes = img.load()
    width, height = imgSize
    shadowOnPixes(pixes, width, height, alpha)


def shadow_file(fileName, outFile, alpha):
    newFile = outFile
    if outFile == None:
        newFile = global_args.auto_outfile(fileName, "_shadow")

    print(f'shadow file with alpha= {alpha}:\n{fileName} \n to {newFile}')

    with Image.open(fileName) as im:
        shadowOnImage(im, alpha)
        im.show()
        im.save(newFile)


def shadow(infile, outfile, recursive, overwrite, alpha=0.5):

    if recursive == None or recursive == False:
        return shadow_file(infile, outfile, alpha)

    infiles = global_args.get_recursive_pic_infiles(infile)
    for infile_for_recursive in infiles:
        shadow_file(infile_for_recursive,
                    infile_for_recursive if overwrite else None,
                    alpha)
