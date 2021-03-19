from PIL import Image, ImageDraw
import aggdraw
from ezpp.utils.color_parser import parse_color_int4

# http://effbot.org/zone/pythondoc-aggdraw.htm

#


def roundrect(img, xy, r,
              pen_color=None,
              brush_color=None,
              border_width=1):
    if r == 0:
        draw = ImageDraw.Draw(img)
        draw.rectangle(xy, fill=brush_color,
                       outline=pen_color, width=border_width)
        return

    pen_color_int4 = None if pen_color is None else parse_color_int4(
        pen_color)
    brush_color_int4 = None if brush_color is None else parse_color_int4(
        brush_color)

    d = aggdraw.Draw(img)
    if brush_color_int4 is not None:
        roundrect_fill(d, xy, r, brush_color_int4)

    if pen_color_int4 is not None:
        roundrect_outline(d, xy, r, pen_color_int4, border_width)

    d.flush()


def roundrect_outline(d, xy, r, pen_color_int4, border_width):
    alpha, red, green, blue = pen_color_int4
    p = aggdraw.Pen((red, green, blue), border_width, opacity=alpha)
    if len(xy) == 2:
        [(x0, y0), (x1, y1)] = xy
    elif len(xy) == 4:
        [x0, y0, x1, y1] = xy
    else:
        print('error args')
        return

    d.line((x0+r, y0, x1-r, y0), p)
    d.line((x0+r, y1, x1-r, y1), p)
    d.line((x0, y0+r, x0, y1-r), p)
    d.line((x1, y0+r, x1, y1-r), p)
    d.arc((x0,  y0, x0+2*r, y0+2*r), 90, 180, p)
    d.arc((x1-2*r,  y0, x1, y0+2*r), 0, 90, p)
    d.arc((x0,  y1-2*r, x0+2*r, y1), 180, 270, p)
    d.arc((x1-2*r, y1-2*r, x1, y1), 270, 360, p)


def roundrect_fill(d, xy, r, brush_color_int4):
    p = None
    alpha, red, green, blue = brush_color_int4
    b = aggdraw.Brush((red, green, blue), opacity=alpha)
    if len(xy) == 2:
        [(x0, y0), (x1, y1)] = xy
    elif len(xy) == 4:
        [x0, y0, x1, y1] = xy
    else:
        print('error args')
        return
    d.rectangle((x0+r, y0, x1-r, y1), p, b)
    d.rectangle((x0, y0+r, x1, y1-r), p, b)
    d.ellipse((x0,  y0, x0+2*r, y0+2*r), p, b)
    d.ellipse((x1-2*r,  y0, x1, y0+2*r), p, b)
    d.ellipse((x0,  y1-2*r, x0+2*r, y1), p, b)
    d.ellipse((x1-2*r, y1-2*r, x1, y1), p, b)


if __name__ == "__main__":
    img = Image.new('RGBA', (400, 300), '#F93')
    roundrect(img, [(40, 50), (140, 250)], 25,
              None, (0xff, 0xff, 0x00, 0x00), 1)
    roundrect(img, [(150, 50), (250, 250)], 25,
              (0xff, 0x00, 0xff, 0x00), None, 1)
    roundrect(img, [(260, 50), (360, 250)], 25,
              (0xff, 0x00, 0x00, 0xff),  (0xff, 0x00, 0xff, 0x00), 3)
    img.show()
