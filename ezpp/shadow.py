#!/usr/bin/env python3
import os
import re
import sys
import argparse
from PIL import Image, ImageColor
from ezutils.colors import *
from . import global_args

COLOR_SAME_RADUS = 160
MIN_TRANSPARENT_ALPHA = int(0.3*0xff)


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
    infile, outfile, recursive, overwrite, preview = global_args.parser_io_argments(
        params)

    alphaStr = params['alpha']
    if not alphaStr:
        alphaStr = '0.5'
    alpha = float(alphaStr)
    shadow(infile, outfile, recursive, overwrite, preview, alpha)


def same_color(colorA, colorB):
    if len(colorA) == 4 and len(colorB) == 4:
        if colorA[3] < MIN_TRANSPARENT_ALPHA and colorB[3] < MIN_TRANSPARENT_ALPHA:
            return True
        elif colorA[3] < MIN_TRANSPARENT_ALPHA or colorB[3] < MIN_TRANSPARENT_ALPHA:
            return False

    r = colorA[0] - colorB[0]
    g = colorA[1] - colorB[1]
    b = colorA[2] - colorB[2]

    return r*r+g*g+b*b < COLOR_SAME_RADUS*COLOR_SAME_RADUS


def shadow_color(colorbg, alpha):
    if len(colorbg) == 4:
        r, g, b, a = colorbg
    else:
        r, g, b = colorbg
        a = 0xff

    if a < MIN_TRANSPARENT_ALPHA:
        r1 = 0
        b1 = 0
        g1 = 0
    else:
        h, s, v = rgb2hsv(r, g, b)
        r1, g1, b1 = hsv2rgb(h, s, (1-alpha)*v)

    str_hex = bytearray([r1, g1, b1, int(0xff*alpha)]).hex()
    return f"#{str_hex}"


def shadow_on_line(pixes, width, height, fromX, fromY, alpha):
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
            if not same_color(first, pixes[x, y]):
                firstObj = pixes[x, y]
            continue

        if same_color(first, pixes[x, y]):
            pixes[x, y] = ImageColor.getcolor(
                shadow_color(pixes[x, y], alpha), "RGBA")


def shadow_on_pixes(pixes, width, height, alpha):
    for i in range(0, width):
        shadow_on_line(pixes, width, height, i, 0, alpha)

    for j in range(1, height):
        shadow_on_line(pixes, width, height, 0, j, alpha)


def shadow_on_image(img, alpha):
    imgSize = img.size
    pixes = img.load()
    width, height = imgSize
    shadow_on_pixes(pixes, width, height, alpha)


def shadow_file(fileName, outFile, preview, alpha):
    newFile = outFile
    if outFile == None:
        newFile = global_args.auto_outfile(fileName, "_shadow")

    print(f'FROM: {fileName}\n shadow file with alpha= {alpha}')

    with Image.open(fileName) as im:
        shadow_on_image(im, alpha)
        if preview:
            print('Preview only')
            im.show()
        else:
            print(f'TO: {newFile}')
            im.save(newFile)


def shadow(infile, outfile, recursive, overwrite, preview, alpha=0.5):

    if recursive == None or recursive == False or preview == True:
        return shadow_file(infile, outfile, preview, alpha)

    infiles = global_args.get_recursive_pic_infiles(infile)
    for infile_for_recursive in infiles:
        shadow_file(infile_for_recursive,
                    infile_for_recursive if overwrite else None,
                    False,
                    alpha)
