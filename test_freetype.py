import freetype  # pip3 install freetype-py

MAX_CHARS_COUNT = 512


def charinfo2char(charinfo):
    charcode, index = charinfo
    return chr(charcode)


# face = freetype.Face("/System/Library/fonts/Menlo.ttc")
# face = freetype.Face("/System/Library/fonts/Symbol.ttf")
# face = freetype.Face("/System/Library/fonts/Apple Braille Outline 6 Dot.ttf")
# face = freetype.Face("/System/Library/fonts/ZapfDingbats.ttf")
# face = freetype.Face("/System/Library/fonts/Apple Color Emoji.ttc")
# face = freetype.Face("/System/Library/fonts/ヒラギノ明朝 ProN.ttc")

def fontchars(fontpath):
    face = freetype.Face("/System/Library/fonts/Supplemental/NISC18030.ttf")
    chars = list(face.get_chars())
    charscount = len(chars)
    print(f'chars({charscount})')
    chars_str = list(map(charinfo2char, chars))[:MAX_CHARS_COUNT]
    for charcode, index in chars:
        print(charcode)
    print(''.join(chars_str))
    if charscount > MAX_CHARS_COUNT:
        print('...')

if __name__ == "__main__":
    print(fontchars("/System/Library/fonts/Supplemental/NISC18030.ttf"))