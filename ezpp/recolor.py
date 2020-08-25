#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter, ImageColor
import argparse
import os
import re
import colorsys
from . import global_args

using_color = "-c The color in hex value in formate of #RRGGBB  or #RGB. For example :#00ff00 or #0f0 make a  green version of your pic"
using_hsv = "HSV:{hue(0-360),saturation[-1.0,1.0],value[-1.0,1.0]},-c will be ignore when using -hsv."
is_color_re = re.compile(r'^#?([0-9a-fA-f]{3}|[0-9a-fA-f]{6})$')
color3_re = re.compile(
    r'^#?([0-9a-fA-F]{1})([0-9a-fA-F]{1})([0-9a-fA-F]{1})$'
)
color6_re = re.compile(
    r'^#?([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})$'
)


def create_cmd_parser(subparsers):
    parser_recolor = subparsers.add_parser(
        'recolor', help='recolor a pic')
    parser_recolor.add_argument("-c", "--color", help=using_color)

    parser_recolor.add_argument("-u", "--hue", help=using_hsv)

    parser_recolor.add_argument("-s", "--saturation", help=using_hsv)

    parser_recolor.add_argument("-v", "--value", help=using_hsv)

    parser_recolor.set_defaults(on_args_parsed=_on_args_parsed)

    return parser_recolor


def repeat2(str_tobe_repeat):
    if len(str_tobe_repeat) > 1:
        return str_tobe_repeat
    return str_tobe_repeat+str_tobe_repeat


def _on_args_parsed(args):
    params = vars(args)
    infile, outfile, recursive, overwrite, preview = global_args.parser_io_argments(
        params)

    color = params['color']
    hue = params['hue']
    saturation = params['saturation']
    value = params['value']
    if hue != None or saturation != None or value != None:
        recolor_hsv(infile, outfile, recursive,
                    overwrite, preview, hue, saturation, value)
        return

    recolor(infile, outfile, recursive, overwrite, preview, color)


def deta_float(origin, deta):
    return max(min(origin + deta, 1.0), 0.0)


def recolor_hsv(infile, outfile, recursive, overwrite, preview, dst_h, dst_s, dst_v):
    if recursive == None or recursive == False or preview == True:
        return recolor_hsv_file(infile, outfile, dst_h, dst_s, dst_v, preview)
    infiles = global_args.get_recursive_pic_infiles(infile)
    for infile_for_recursive in infiles:
        recolor_hsv_file(infile_for_recursive,
                         infile_for_recursive if overwrite else None,
                         dst_h,
                         dst_s,
                         dst_v,
                         False)


def recolor_hsv_file(infile, outfile, dst_h, dst_s, dst_v, preview):
    # name of new file
    # 确定用什么样的文件名来保存图片
    # print(f"dst_h:{dst_h}, dst_s:{dst_s}, dst_v:{dst_v}")
    hsv_name = f"_h({dst_h})" if dst_h != None else f""
    hsv_name += f"_s({dst_s})" if dst_s != None else f""
    hsv_name += f"_v({dst_v})" if dst_v != None else f""

    new_filename = outfile if outfile else global_args.auto_outfile(
        infile, f"_hsv{hsv_name}")

    print(f"FROM: {infile} + hsv{hsv_name}")

    # load pixel from image.
    # 打开图片，加载像素值
    with open(infile, 'rb') as imgf:
        img = Image.open(imgf).convert('RGBA')
    width = img.width
    height = img.height
    px = img.load()

    # new file to save result of recolor
    # 创造一个新图片用来保存变换结果
    img_new = Image.new('RGBA', (width, height))
    px_new = img_new.load()

    # recolor every pixel
    # 逐个像素变换
    for y in range(0, height):
        for x in range(0, width):
            r, g, b, a = px[x, y]
            h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
            new_s = s if r == g and g == b else (
                deta_float(s, float(dst_s)) if dst_s != None else s
            )
            rn, gn, bn = colorsys.hsv_to_rgb(
                float(dst_h)/float(360) if dst_h != None else h,
                new_s,
                deta_float(v, float(dst_v)) if dst_v != None else v)

            px_new[x, y] = (int(255*rn), int(255*gn), int(255*bn), a)

    if preview:
        print("Preview Only")
        img_new.show()
    else:
        filename, ext = os.path.splitext(infile)
        print("TO:", new_filename)
        # RGBA for png ,And RGB for other ext
        # 如果输入文件是PNG保留RGBA格式，其他文件使用RGB格式。
        if ext.lower() == '.png':
            img_new.save(new_filename, 'PNG')
        else:
            img_new.convert('RGB').save(new_filename)


def recolor(infile, outfile, recursive, overwrite, preview, color):
    if recursive == None or recursive == False or preview == True:
        return recolor_file(infile, outfile, preview, color)
    infiles = global_args.get_recursive_pic_infiles(infile)
    for infile_for_recursive in infiles:
        recolor_file(infile_for_recursive,
                     infile_for_recursive if overwrite else None,
                     False,
                     color)


def recolor_file(infile, outfile, preview, color):

    if not is_color_re.match(color):
        print(using_color+using_hsv)
        exit(2)

    color_re = color6_re if len(color) > 4 else color3_re
    color_m = color_re.match(color)
    red = repeat2(color_m.group(1))
    green = repeat2(color_m.group(2))
    blue = repeat2(color_m.group(3))
    # src_h, src_s, src_v = colorsys.rgb_to_hsv(0, 152/255, 1)
    dst_h, dst_s, dst_v = colorsys.rgb_to_hsv(
        int(red, base=16)/255,
        int(green, base=16)/255,
        int(blue, base=16)/255)

    color = f"{red}{green}{blue}"
    new_filename = outfile if outfile else global_args.auto_outfile(
        infile, f"_0x{color}")

    print(f"hue -> {dst_h}")
    print(f"FROM: {infile} + #{color}")

    with open(infile, 'rb') as imgf:
        img = Image.open(imgf).convert('RGBA')

    width = img.width
    height = img.height
    px = img.load()

    img_new = Image.new('RGBA', (width, height))
    px_new = img_new.load()

    for y in range(0, height):
        for x in range(0, width):
            r, g, b, a = px[x, y]
            h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
            rn, gn, bn = colorsys.hsv_to_rgb(dst_h, s, v)
            px_new[x, y] = (int(255*rn), int(255*gn), int(255*bn), a)
    if preview:
        print("Preview Only")
        img_new.show()
    else:
        print(f"To: {new_filename}")
        bar_filename, ext = os.path.splitext(infile)
        # RGBA for png ,And RGB for other ext
        # 如果输入文件是PNG保留RGBA格式，其他文件使用RGB格式。
        if ext.lower == '.png':
            img_new.save(new_filename)
        else:
            img_new.convert('RGB').save(new_filename)
