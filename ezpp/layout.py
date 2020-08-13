#!/usr/bin/env python3
import argparse
import os
import re
from . import global_args
import yaml 
import json
from ezutils.files import readstr
from pydash import _
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter, ImageColor

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
    infile, outfile, r, o = global_args.parser_io_argments(params)

    params_str = params['params']
    
    if not params_str:
        params_str = '{}'
    params_map = json.loads(params_str)
    layout(infile, outfile, params_map)


def layout(infile, outfile,params_map):
    dataStr = readstr(infile)
    yamlCfg = yaml.load(dataStr)
    print('cfg:',yamlCfg)
    print('map:',params_map)

    width = int(_.get(yamlCfg,'canvas.width'))
    height = int(_.get(yamlCfg,'canvas.height'))
    antialias_size =int(_.get(yamlCfg,'canvas.antialias_size'))
    color =  _.get(yamlCfg,'canvas.color')
    if color == None:
        color = '#fff'
    img = Image.new('RGB', (width*antialias_size, height*antialias_size), color)
    # draw = ImageDraw.Draw(img)
    if antialias_size > 1:
        img = img.resize((width, height), Image.ANTIALIAS)
    img.show()

