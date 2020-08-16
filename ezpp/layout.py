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

def render_layer(img, layer, infile_dir):
    type = _.get(layer,'type')
    if type == "image":
        file_name = _.get(layer,'filename')
        layer_image = Image.open(os.path.join(infile_dir,file_name)).convert("RGBA")
        layer_image.show()
        print('img.mode',img.mode)
        print('layer_image.mode',layer_image.mode)
        # new_image = Image.alpha_composite(img, layer_image)
        img.paste(layer_image,(0,0),mask=layer_image)
        # img.show()
    pass

def merge_params(data_str,params):
    tmp_yaml_cfg = yaml.load(data_str)
    cfg_params = _.get(tmp_yaml_cfg,'params');
    for cfg_param in cfg_params:
        data_str = data_str.replace(f"__{cfg_param}__",params[cfg_param])
    print("new data_str:\n",data_str)
    return data_str

def layout(infile, outfile,params_map):
    data_str = readstr(infile)
    infile_dir,infile_name = os.path.split(infile)
    # print('data_str:',data_str)
    yaml_cfg = yaml.load(merge_params(data_str,params_map))
    print('yaml_cfg',yaml_cfg)

    width = int(_.get(yaml_cfg,'canvas.width'))
    height = int(_.get(yaml_cfg,'canvas.height'))
    antialias_size =int(_.get(yaml_cfg,'canvas.antialias_size'))
    
    color =  _.get(yaml_cfg,'canvas.color')
    if color == None:
        color = '#fff'
    img = Image.new('RGBA', (width*antialias_size, height*antialias_size), color)

    layers = _.get(yaml_cfg, 'layers')
    for layer in layers:
        render_layer(img, layer, infile_dir)

    if antialias_size > 1:
        img = img.resize((width, height), Image.ANTIALIAS)
    img.show()

    