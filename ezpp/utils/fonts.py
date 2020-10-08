import freetype


def get_sample_text(font_path):
    face = freetype.Face(font_path)
    DEF_SAMPLE = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sample = DEF_SAMPLE
    try:
        sample = face.get_best_name_string(
            freetype.TT_NAME_ID_SAMPLE_TEXT, DEF_SAMPLE)
        sample = sample.replace('\n', ' ')
    except:
        sample = DEF_SAMPLE

    return sample


if __name__ == "__main__":
    from ezpp import global_args
    font_exts = ['ttf', 'ttc', 'otf', 'dfont']
    fonts = global_args.get_recursive_infiles_by_ext(
        '/System/Library/fonts', font_exts)
    for font_path in fonts:
        print(font_path)
        print(get_sample_text(font_path))
