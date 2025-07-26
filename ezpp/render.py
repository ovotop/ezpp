#!/usr/bin/env python3
from ezpp.shadow import shadow_on_image
import os
from . import global_args
import yaml
import json
from ezutils.files import readstr
from pydash import _
from PIL import Image, ImageDraw, ImageFont
from ezpp.utils.text import text_by_pos_str
from ezpp.utils.roundrect import roundrect
from ezpp.utils.size_parser import parse_position
import re


def create_cmd_parser(subparsers):
    cmd_parser = subparsers.add_parser(
        'render', help='render help')
    cmd_parser.add_argument("-a",
                            "--arguments",
                            help='params,like"{w:960,h:540,title:"hello"}"')
    cmd_parser.add_argument("-c",
                            "--config",
                            help='yml config file for params')
    cmd_parser.add_argument("--silent",
                            action='store_true',
                            help='render silently. with out stdout')

    cmd_parser.set_defaults(on_args_parsed=_on_args_parsed)

    return cmd_parser


def convert_js_obj_to_json(js_obj_str):
    # 正则表达式模式：匹配键（标识符）并加上双引号
    pattern = r'([{,]\s*)([a-zA-Z_]\w*)(\s*:)'
    # 替换：在键的两侧加上双引号
    fixed_str = re.sub(pattern, r'\1"\2"\3', js_obj_str)
    return fixed_str


def parse_args(params_str):
    new_params_str = convert_js_obj_to_json(params_str)
    print(f"params_str: {params_str}")
    print(f"new_params_str: {new_params_str}")
    params_map = json.loads(new_params_str)  # 标准 JSON 作为备选
    return params_map


def _on_args_parsed(args):
    params = vars(args)
    infile, outfile, r, o, preview = global_args.parser_io_argments(params)
    params_map = None
    silent = False
    params_str = params['arguments']
    config_str = params['config']

    if config_str:
        params_map = read_yml_config(config_str, "params")
        print(f"parmas1: {params_map}")
    else:
        print(f"params_str: {params_str}")
        silent = params['silent']
        if not params_str:
            params_str = '{}'
        # params_map = json.loads(params_str)
        params_map = parse_args(params_str)  # 支持 JS 对象语法
        print(f"parmas3: {params_map}")

    render(infile, outfile, params_map, preview, silent)


def read_yml_config(config_file, key_str):
    if not os.path.exists(config_file):
        return None

    config_str = readstr(config_file)
    config_map = yaml.load(config_str, Loader=yaml.FullLoader)
    return config_map.get(key_str)


def render_canvas_file(infile, params_map, antialias_size=1):
    data_str = readstr(infile)
    infile_dir, infile_name = os.path.split(infile)
    yaml_cfg = yaml.load(merge_params(data_str, params_map),
                         Loader=yaml.FullLoader)
    return render_canvas(yaml_cfg, infile_dir, params_map,
                         antialias_parent=antialias_size)


def render_canvas(yaml_cfg, infile_dir, params_map, antialias_parent=1):
    width = int(_.get(yaml_cfg, 'canvas.width'))
    height = int(_.get(yaml_cfg, 'canvas.height'))
    # int(_.get(yaml_cfg, 'canvas.antialias_size', '1'))
    cfg_antialias_size = 1
    antialias_size = cfg_antialias_size * antialias_parent
    # canvas
    color = _.get(yaml_cfg, 'canvas.color')
    if color is None:
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
    item_visible = _.get(item, 'visible', True)
    if not item_visible:
        return

    item_type = _.get(item, 'type')

    if item_type == "image":
        render_image_item(img, item, infile_dir, antialias_size)
    elif item_type == "text":
        render_text_item(img, item, infile_dir, antialias_size=antialias_size)
    elif item_type == "rect":
        render_rect_item(img, item, infile_dir, params_map, antialias_size)
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
    x = (posx * antialias_size) if isinstance(posx, str) else posx
    posy = _.get(item, 'pos.y')
    y = (posy * antialias_size) if isinstance(posy, str) else posy
    w, h = img.size

    layer_w, layer_h = layer_img.size
    x_int = parse_position(w-layer_w, x)
    y_int = parse_position(h-layer_h, y)
    img.paste(layer_img, (x_int, y_int), mask=layer_img)


def render_rect_item(img, item, infile_dir, params_map, antialias_size):
    posx = _.get(item, 'pos.x')
    x = (posx * antialias_size) if isinstance(posx, str) else posx
    posy = _.get(item, 'pos.y')
    y = (posy * antialias_size) if isinstance(posy, str) else posy
    w, h = img.size

    sizew = _.get(item, 'size.w')
    width = int(sizew) * int(antialias_size)
    sizeh = _.get(item, 'size.h')
    height = int(sizeh) * int(antialias_size)

    x_int = parse_position(w-width, x)
    y_int = parse_position(h-height, y)

    xy = [x_int, y_int, x_int + width, y_int + height]

    radius = int(_.get(item, 'radius', 0))
    border_color = _.get(item, 'border_color', None)
    fill_color = _.get(item, 'fill_color', None)
    border_size = int(_.get(item, 'border_size', '1'))
    roundrect(img, xy, radius,
              pen_color=border_color,
              brush_color=fill_color,
              border_width=border_size)


def render_text_item(img, item, infile_dir, antialias_size=1):
    title = _.get(item, 'title')
    font_size = _.get(item, 'font.size')
    font_filename = _.get(item, 'font.filename')
    font_filepath = _.get(item, 'font.path')
    font_path = font_filepath if font_filepath is not None else os.path.join(
        infile_dir, font_filename)
    color = _.get(item, 'font.color')
    font = ImageFont.truetype(
        font_path,
        font_size * antialias_size
    )

    posx = _.get(item, 'pos.x')
    x = (posx * antialias_size) if isinstance(posx, str) else posx
    posy = _.get(item, 'pos.y')
    y = (posy * antialias_size) if isinstance(posy, str) else posy

    w, h = img.size
    # 文本在图片上的大小
    layer_w, layer_h = getsize(font, title)
    x_int = parse_position(w-layer_w, x)
    y_int = parse_position(h-layer_h, y)
    text_by_pos_str(title, color, font, img, x_int, y_int)


def getsize(font, txt):
    """Get the size of the text."""
    bbox = font.getbbox(txt)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


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
    if params is None:
        return data_str

    tmp_yaml_cfg = yaml.load(data_str, Loader=yaml.FullLoader)
    cfg_params = _.get(tmp_yaml_cfg, 'params')
    if cfg_params is None:
        return data_str

    for cfg_param in cfg_params:
        if isinstance(cfg_param, str):
            print(f"params = {params} ; cfg_param = {cfg_param}")
            print(f"replaceing __{cfg_param}__ with {params[cfg_param]}")
            data_str = data_str.replace(f"__{cfg_param}__", params[cfg_param])
        else:
            name = _.get(cfg_param, 'name', None)
            if name is None:
                continue
            default = _.get(cfg_param, 'default')
            value = _.get(params, name, default)
            print(f"replaceing __{name}__ with {value} default {default}")
            data_str = data_str.replace(f"__{name}__", f"{value}")

    return data_str


def default_outfile(infile):
    filename, ext = os.path.splitext(infile)
    return f"{filename}.png"


def render(infile, outfile, params_map, preview, silent):
    print(f"render {params_map}")
    if not silent:
        print("FROM:", infile)

    newfile = outfile if outfile else default_outfile(infile)

    img = render_canvas_file(infile, params_map)
    if preview:
        if not silent:
            print("Preview Only")
        img.show()
    else:
        if not silent:
            print("TO:", newfile)
        img.save(newfile, 'PNG')
