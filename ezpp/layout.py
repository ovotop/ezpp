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
from ezpp.utils.text import text_horzontal_center,text_vertical_center,text_center
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

def render_image_layer(img, layer, infile_dir):
    x = _.get(layer, 'pos.x')
    y = _.get(layer, 'pos.y')
    w,h = img.size

    file_name = _.get(layer,'filename')
    layer_image = Image.open(os.path.join(infile_dir,file_name)).convert("RGBA")
    layer_w, layer_h = layer_image.size
    
    if x == "center":
        x = int((w-layer_w)/2)
    
    if y == "center":
        y = int((h-layer_h)/2)

    img.paste(layer_image,(x,y),mask=layer_image)


def render_text_layer(img, layer, infile_dir):
    title = _.get(layer, 'title')
    font_size = _.get(layer, 'font.size')
    font_name = _.get(layer, 'font.name')
    color = _.get(layer, 'font.color')
    font = ImageFont.truetype(
        font_name,
        font_size
    )
    x = _.get(layer, 'pos.x')
    y = _.get(layer, 'pos.y')
    w,h = img.size
    if x == "center" and y == "center":
        text_center(title, color, font, img, w, h)
    elif x == "center":
        text_horzontal_center(title, color, font, img, w, y)
    elif y == "center":
        text_vertical_center(title, color, font, img, h, x)
    else:
        draw = ImageDraw.Draw(img)
        draw.text((x, y), title, color, font=font)

def render_layer(img, layer, infile_dir):
    layer_type = _.get(layer,'type')
    if layer_type == "image":
        render_image_layer(img, layer, infile_dir)
    elif layer_type == "text":
        render_text_layer(img, layer, infile_dir)

def merge_params(data_str,params):
    tmp_yaml_cfg = yaml.load(data_str)
    cfg_params = _.get(tmp_yaml_cfg, 'params');
    for cfg_param in cfg_params:
        data_str = data_str.replace(f"__{cfg_param}__", params[cfg_param])
    print("new data_str:\n",data_str)
    return data_str

def layout(infile, outfile, params_map):
    data_str = readstr(infile)
    infile_dir, infile_name = os.path.split(infile)
    # print('data_str:',data_str)
    yaml_cfg = yaml.load(merge_params(data_str, params_map))
    print('yaml_cfg',yaml_cfg)

    width = int(_.get(yaml_cfg, 'canvas.width'))
    height = int(_.get(yaml_cfg, 'canvas.height'))
    antialias_size =int(_.get(yaml_cfg, 'canvas.antialias_size'))
    
    color =  _.get(yaml_cfg, 'canvas.color')
    if color == None:
        color = '#fff'
    img = Image.new('RGBA', (width*antialias_size, height*antialias_size), color)

    layers = _.get(yaml_cfg, 'layers')
    for layer in layers:
        render_layer(img, layer, infile_dir)

    if antialias_size > 1:
        img = img.resize((width, height), Image.ANTIALIAS)
    img.show()

    