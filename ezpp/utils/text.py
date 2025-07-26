from ezpp.utils.size_parser import parse_position
from PIL import ImageDraw


def getsize(font, txt):
    """Get the size of the text."""
    bbox = font.getbbox(txt)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


def text_horzontal_center(text, color, font, img, canvas_width, base_y):
    text_width, text_height = getsize(font, text)
    draw = ImageDraw.Draw(img)
    x = (canvas_width-text_width)/2
    y = base_y-text_height
    draw.text((x, y), text, color, font=font)


def text_vertical_center(text, color, font, img, canvas_height, base_x):
    text_width, text_height = getsize(font, text)
    draw = ImageDraw.Draw(img)
    x = base_x
    y = (canvas_height-text_height)/2
    draw.text((x, y), text, color, font=font)


def text_center(text, color, font, img):
    canvas_width, canvas_height = img.size
    text_width, text_height = getsize(font, text)
    draw = ImageDraw.Draw(img)
    x = (canvas_width-text_width)/2
    y = (canvas_height-text_height)/2
    draw.text((x, y), text, color, font=font)


def text_by_pos_str(text, color, font, img, pos_str_x, pos_str_y):
    canvas_width, canvas_height = img.size
    x = parse_position(canvas_width, pos_str_x)
    y = parse_position(canvas_height, pos_str_y)
    draw = ImageDraw.Draw(img)
    draw.text((x, y), text, color, font=font)
