from PIL import Image
import aggdraw
# http://effbot.org/zone/pythondoc-aggdraw.htm


def roundrect(img, xy, r,
              pen_color=0xFFFFFFFF,
              brush_color=None,
              border_width=1):
    d = aggdraw.Draw(img)
    if brush_color is not None:
        roundrect_fill(d, xy, r, brush_color)

    if pen_color is not None:
        roundrect_outline(d, xy, r, pen_color, border_width)

    d.flush()


def roundrect_outline(d, xy, r, pen_color, border_width):
    p = aggdraw.Pen(pen_color, border_width)
    [(x0, y0), (x1, y1)] = xy
    d.line((x0+r, y0, x1-r, y0), p)
    d.line((x0+r, y1, x1-r, y1), p)
    d.line((x0, y0+r, x0, y1-r), p)
    d.line((x1, y0+r, x1, y1-r), p)
    d.arc((x0,  y0, x0+2*r, y0+2*r), 90, 180, p)
    d.arc((x1-2*r,  y0, x1, y0+2*r), 0, 90, p)
    d.arc((x0,  y1-2*r, x0+2*r, y1), 180, 270, p)
    d.arc((x1-2*r, y1-2*r, x1, y1), 270, 360, p)


def roundrect_fill(d, xy, r, brush_color):
    p = None
    b = aggdraw.Brush(brush_color)
    [(x0, y0), (x1, y1)] = xy
    d.rectangle((x0+r, y0, x1-r, y1), p, b)
    d.rectangle((x0, y0+r, x1, y1-r), p, b)
    d.ellipse((x0,  y0, x0+2*r, y0+2*r), p, b)
    d.ellipse((x1-2*r,  y0, x1, y0+2*r), p, b)
    d.ellipse((x0,  y1-2*r, x0+2*r, y1), p, b)
    d.ellipse((x1-2*r, y1-2*r, x1, y1), p, b)


if __name__ == "__main__":
    img = Image.new('RGBA', (400, 300), '#F93')
    roundrect(img, [(40, 50), (140, 250)], 25, None, 0xFF00FF00)
    roundrect(img, [(150, 50), (250, 250)], 25, 0xFFFFFFFF, None, 1)
    roundrect(img, [(260, 50), (360, 250)], 25, 0xFFFFFFFF, 0xFF00FF00, 3)
    img.show()
