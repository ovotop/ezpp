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
from ezpp.utils.text import text_horzontal_center, text_vertical_center, text_center
from ezpp.shadow import shadow_on_image


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
    preview = params['preview']
    if not params_str:
        params_str = '{}'
    params_map = json.loads(params_str)
    layout(infile, outfile, params_map, preview)


def render_canvas_file(infile, params_map):
    data_str = readstr(infile)
    infile_dir, infile_name = os.path.split(infile)
    yaml_cfg = yaml.load(merge_params(data_str, params_map),
                         Loader=yaml.FullLoader)
    return render_canvas(yaml_cfg, infile_dir, params_map)


def render_canvas(yaml_cfg, infile_dir, params_map):
    width = int(_.get(yaml_cfg, 'canvas.width'))
    height = int(_.get(yaml_cfg, 'canvas.height'))
    antialias_size = int(_.get(yaml_cfg, 'canvas.antialias_size', '1'))

    # canvas
    color = _.get(yaml_cfg, 'canvas.color')
    if color == None:
        color = '#fff'
    img = Image.new('RGBA', (width*antialias_size,
                             height*antialias_size), color)

    # items
    img_layers = Image.new(
        'RGBA', (width*antialias_size, height*antialias_size), ("#0000"))
    items = _.get(yaml_cfg, 'items')
    for layer in items:
        render_layer(img_layers, layer, infile_dir, params_map)

    img.paste(img_layers, (0, 0), mask=img_layers)

    if antialias_size > 1:
        img = img.resize((width, height), Image.ANTIALIAS)
    return img


def render_layer(img, layer, infile_dir, params_map):
    layer_type = _.get(layer, 'type')
    if layer_type == "image":
        render_image_layer(img, layer, infile_dir)
    elif layer_type == "text":
        render_text_layer(img, layer, infile_dir)
    elif layer_type == "shadow":
        render_shadow_layer(img, layer)
    elif layer_type == "import":
        render_import_layer(img, layer, infile_dir, params_map)
    elif layer_type == "nested":
        render_nested_layer(img, layer, infile_dir, params_map)


def render_image_layer(img, layer, infile_dir):
    file_name = _.get(layer, 'filename')
    layer_img = Image.open(os.path.join(infile_dir, file_name)).convert("RGBA")
    paste_layer_img(img, layer, layer_img, infile_dir)


def paste_layer_img(img, layer, layer_img, infile_dir):
    x = _.get(layer, 'pos.x')
    y = _.get(layer, 'pos.y')
    w, h = img.size

    layer_w, layer_h = layer_img.size

    if x == "center":
        x = int((w-layer_w)/2)

    if y == "center":
        y = int((h-layer_h)/2)
    img.paste(layer_img, (x, y), mask=layer_img)


def render_text_layer(img, layer, infile_dir):
    title = _.get(layer, 'title')
    font_size = _.get(layer, 'font.size')
    font_filename = _.get(layer, 'font.filename')
    font_filepath = _.get(layer, 'font.path')
    font_path = font_filepath if font_filepath != None else os.path.join(
        infile_dir, font_filename)
    color = _.get(layer, 'font.color')
    font = ImageFont.truetype(
        font_path,
        font_size
    )
    x = _.get(layer, 'pos.x')
    y = _.get(layer, 'pos.y')
    w, h = img.size
    if x == "center" and y == "center":
        text_center(title, color, font, img, w, h)
    elif x == "center":
        text_horzontal_center(title, color, font, img, w, y)
    elif y == "center":
        text_vertical_center(title, color, font, img, h, x)
    else:
        draw = ImageDraw.Draw(img)
        draw.text((x, y), title, color, font=font)


def render_shadow_layer(img, layer):
    alpha = _.get(layer, 'alpha')
    shadow_on_image(img, alpha)


def merge_dicts(dict1, dict2):
    res = {**dict1, **dict2}
    return res


def render_import_layer(img, layer, infile_dir, params_map):
    filename = _.get(layer, 'filename')
    params = _.get(layer, 'params')
    new_params = merge_dicts(params_map, params) if params else params_map
    layer_img = render_canvas_file(
        os.path.join(infile_dir, filename), new_params)
    paste_layer_img(img, layer, layer_img, infile_dir)


def render_nested_layer(img, layer, infile_dir, params_map):
    layer_img = render_canvas(layer, infile_dir, params_map)
    paste_layer_img(img, layer, layer_img, infile_dir)


def merge_params(data_str, params):
    if params == None:
        return data_str

    tmp_yaml_cfg = yaml.load(data_str, Loader=yaml.FullLoader)
    cfg_params = _.get(tmp_yaml_cfg, 'params')
    if cfg_params == None:
        return data_str

    for cfg_param in cfg_params:
        data_str = data_str.replace(f"__{cfg_param}__", params[cfg_param])
    return data_str


def default_outfile(infile):
    filename, ext = os.path.splitext(infile)
    return f"{filename}.png"


def layout(infile, outfile, params_map, preview):
    print("FROM:", infile)
    newfile = outfile if outfile else default_outfile(infile)

    img = render_canvas_file(infile, params_map)
    if preview:
        print("Preview Only")
        img.show()
    else:
        print("TO:", newfile)
        img.save(newfile)
