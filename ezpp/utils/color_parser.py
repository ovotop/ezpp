import re

using_color = "-c The color in hex value in formate of #RRGGBB  or #RGB. For example :#00ff00 or #0f0 make a  green version of your pic"
is_color_re = re.compile(r'^#?([0-9a-fA-f]{3}|[0-9a-fA-f]{6})$')
color3_re = re.compile(
    r'^#?([0-9a-fA-F]{1})([0-9a-fA-F]{1})([0-9a-fA-F]{1})$'
)

color4_re = re.compile(
    r'^#?([0-9a-fA-F]{1})([0-9a-fA-F]{1})([0-9a-fA-F]{1})([0-9a-fA-F]{1})$'
)

color6_re = re.compile(
    r'^#?([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})$'
)

color8_re = re.compile(
    r'^#?([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})([0-9a-fA-F]{2})$'
)

re_strs = [None, None, None, None, color3_re,
           color4_re, None, color6_re, None, color8_re]


def repeat2(str_tobe_repeat):
    if len(str_tobe_repeat) > 1:
        return str_tobe_repeat
    return str_tobe_repeat+str_tobe_repeat


def parse_color4(color):
    color_re = re_strs[len(color)]
    if color_re is None:
        return ('FF', 'FF', 'FF', 'FF')

    color_m = color_re.match(color)
    alpha = 'FF'
    if len(color_m.groups()) == 3:
        red = repeat2(color_m.group(1))
        green = repeat2(color_m.group(2))
        blue = repeat2(color_m.group(3))
    else:
        alpha = repeat2(color_m.group(1))
        red = repeat2(color_m.group(2))
        green = repeat2(color_m.group(3))
        blue = repeat2(color_m.group(4))
    return (alpha, red, green, blue)


def parse_color_int4(color):
    alpha, red, green, blue = parse_color4(color)
    return(
        int(alpha, base=16),
        int(red, base=16),
        int(green, base=16),
        int(blue, base=16))


def parse_color_int(color):
    alpha, red, green, blue = parse_color4(color)
    return int(f'0x{alpha:2}{red:2}{green:2}{blue:2}', base=16)
