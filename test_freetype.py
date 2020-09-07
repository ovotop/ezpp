import freetype


def charinfo2char(charinfo):
    charcode, index = charinfo
    return chr(charcode)


face = freetype.Face("/System/Library/fonts/Menlo.ttc")
print(face.num_charmaps)
chars = list(face.get_chars())[:350]
chars_str = list(map(charinfo2char, chars))
# for charcode, index in chars:
#     print(chr(charcode))
print(''.join(chars_str))
