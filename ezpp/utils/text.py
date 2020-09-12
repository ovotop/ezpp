from PIL import ImageDraw
SHOW_BOUNDS = False


def text_horzontal_center(text, color, font, img, canvas_width, base_y):
    text_width, text_height = font.getsize(text)
    draw = ImageDraw.Draw(img)
    x = (canvas_width-text_width)/2
    y = base_y-text_height
    if SHOW_BOUNDS:
        draw.rectangle([(x, y), (x+text_width, y+text_height)])
    draw.text((x, y), text, color, font=font)


def text_vertical_center(text, color, font, img, canvas_height, base_x):
    text_width, text_height = font.getsize(text)
    draw = ImageDraw.Draw(img)
    x = base_x
    y = (canvas_height-text_height)/2
    if SHOW_BOUNDS:
        draw.rectangle([(x, y), (x+text_width, y+text_height)])
    draw.text((x, y), text, color, font=font)


def text_center(text, color, font, img, canvas_width, canvas_height):
    text_width, text_height = font.getsize(text)
    draw = ImageDraw.Draw(img)
    x = (canvas_width-text_width)/2
    y = (canvas_height-text_height)/2
    if SHOW_BOUNDS:
        draw.rectangle([(x, y), (x+text_width, y+text_height)])
    draw.text((x, y), text, color, font=font)
