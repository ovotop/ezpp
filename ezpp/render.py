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
        'render', help='render help')
    cmd_parser.add_argument("-a",
                            "--arguments",
                            help='params map,like \"{w:960,h:540,title:"hello"}\"')

    cmd_parser.set_defaults(on_args_parsed=_on_args_parsed)

    return cmd_parser


def _on_args_parsed(args):
    params = vars(args)
    infile, outfile, r, o, preview = global_args.parser_io_argments(params)

    params_str = params['arguments']
    if not params_str:
        params_str = '{}'
    params_map = json.loads(params_str)
    render(infile, outfile, params_map, preview)


def render_canvas_file(infile, params_map, antialias_size=1):
    data_str = readstr(infile)
    infile_dir, infile_name = os.path.split(infile)
    yaml_cfg = yaml.load(merge_params(data_str, params_map),
                         Loader=yaml.FullLoader)
    return render_canvas(yaml_cfg, infile_dir, params_map, antialias_parent=antialias_size)


def render_canvas(yaml_cfg, infile_dir, params_map, antialias_parent=1):
    width = int(_.get(yaml_cfg, 'canvas.width'))
    height = int(_.get(yaml_cfg, 'canvas.height'))
    cfg_antialias_size = int(_.get(yaml_cfg, 'canvas.antialias_size', '1'))
    antialias_size = cfg_antialias_size * antialias_parent
    # canvas
    color = _.get(yaml_cfg, 'canvas.color')
    if color == None:
        color = '#fff'
    img = Image.new('RGBA', (width*antialias_size,
                             height*antialias_size), color)

    # items
    img_items = Image.new(
        'RGBA', (width*antialias_size, height*antialias_size), ("#0000"))
    items = _.get(yaml_cfg, 'items')
    for item in items:
        render_item(img_items, item, infile_dir, params_map,
                    antialias_size=antialias_size)

    img.paste(img_items, (0, 0), mask=img_items)
    if antialias_size > 1:
        resize_width = int(width*antialias_parent)
        resize_height = int(height * antialias_parent)
        img = img.resize((resize_width, resize_height), Image.ANTIALIAS)
    return img


def render_item(img, item, infile_dir, params_map, antialias_size=1):
    item_type = _.get(item, 'type')
    if item_type == "image":
        render_image_item(img, item, infile_dir, antialias_size)
    elif item_type == "text":
        render_text_item(img, item, infile_dir, antialias_size=antialias_size)
    elif item_type == "shadow":
        render_shadow_item(img, item)
    elif item_type == "import":
        render_import_item(img, item, infile_dir, params_map, antialias_size)
    elif item_type == "nested":
        render_nested_item(img, item, infile_dir, params_map, antialias_size)


def render_image_item(img, item, infile_dir, antialias_size=1):
    file_name = _.get(item, 'filename')
    layer_img = Image.open(os.path.join(infile_dir, file_name)).convert("RGBA")
    paste_item_img(img, item, layer_img, infile_dir, antialias_size)


def paste_item_img(img, item, layer_img, infile_dir, antialias_size=1):
    posx = _.get(item, 'pos.x')
    x = (posx * antialias_size) if type(posx) != type("str") else posx
    posy = _.get(item, 'pos.y')
    y = (posy * antialias_size) if type(posy) != type("str") else posy
    w, h = img.size

    layer_w, layer_h = layer_img.size
    if x == "center":
        x = int((w-layer_w)/2)

    if y == "center":
        y = int((h-layer_h)/2)
    img.paste(layer_img, (x, y), mask=layer_img)


def render_text_item(img, item, infile_dir, antialias_size=1):
    title = _.get(item, 'title')
    font_size = _.get(item, 'font.size')
    font_filename = _.get(item, 'font.filename')
    font_filepath = _.get(item, 'font.path')
    font_path = font_filepath if font_filepath != None else os.path.join(
        infile_dir, font_filename)
    color = _.get(item, 'font.color')
    font = ImageFont.truetype(
        font_path,
        font_size * antialias_size
    )
    posx = _.get(item, 'pos.x')
    x = (posx * antialias_size) if type(posx) != type("str") else posx
    posy = _.get(item, 'pos.y')
    y = (posy * antialias_size) if type(posy) != type("str") else posy

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


def render_shadow_item(img, item):
    alpha = _.get(item, 'alpha')
    shadow_on_image(img, alpha)


def merge_dicts(dict1, dict2):
    res = {**dict1, **dict2}
    return res


def render_import_item(img, item, infile_dir, params_map, antialias_size=1):
    filename = _.get(item, 'filename')
    params = _.get(item, 'params')
    new_params = merge_dicts(params_map, params) if params else params_map
    layer_img = render_canvas_file(
        os.path.join(infile_dir, filename),
        new_params,
        antialias_size)
    paste_item_img(img, item, layer_img, infile_dir, antialias_size)


def render_nested_item(img, item, infile_dir, params_map, antialias_size=1):
    layer_img = render_canvas(item, infile_dir, params_map,
                              antialias_parent=antialias_size)
    paste_item_img(img, item, layer_img, infile_dir, antialias_size)


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


def render(infile, outfile, params_map, preview):
    print("FROM:", infile)
    newfile = outfile if outfile else default_outfile(infile)

    img = render_canvas_file(infile, params_map)
    if preview:
        print("Preview Only")
        img.show()
    else:
        print("TO:", newfile)
        img.save(newfile, 'PNG')
