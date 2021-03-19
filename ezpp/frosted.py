#!/usr/bin/env python3
from PIL import Image, ImageFilter
from . import global_args


def create_cmd_parser(subparsers):
    parser_frosted = subparsers.add_parser(
        'frosted', help='frosted glass on a pic')
    parser_frosted.add_argument("-s",
                                "--size",
                                help="size of frosted range,"
                                " default 10, recommonded [3,20]")
    parser_frosted.set_defaults(on_args_parsed=_on_args_parsed)

    return parser_frosted


def repeat2(str_tobe_repeat):
    if len(str_tobe_repeat) > 1:
        return str_tobe_repeat
    return str_tobe_repeat+str_tobe_repeat


def _on_args_parsed(args):
    params = vars(args)
    i, o, recursive, overwrite, preview = global_args.parser_io_argments(
        params)

    sizeStr = params['size']
    if not sizeStr:
        sizeStr = '10'

    size = int(sizeStr)
    mode = 5
    if size:
        if size > 5:
            mode = 5
        elif size > 3:
            mode = 3
        else:
            mode = 0

        frosted(i, o, recursive, overwrite, preview, size, mode)
    else:
        frosted(i, o, recursive, overwrite, preview)


def frosted(infile, outfile, recursive, overwrite, preview,
            blurSize=10, mode=5):
    print('frosted', preview)
    if recursive is None or not recursive or preview:
        return frosted_file(infile, outfile, preview, blurSize, mode)
    infiles = global_args.get_recursive_pic_infiles(infile)
    for infile_for_recursive in infiles:
        frosted_file(infile_for_recursive,
                     infile_for_recursive if overwrite else None,
                     False,
                     blurSize,
                     mode)


def frosted_file(infile, outfile, preview, blurSize=10, mode=5):
    new_filename = outfile
    if outfile is None:
        new_filename = global_args.auto_outfile(infile, '_frosted')

    print(f"Frome: {infile} frosted(size = {blurSize})")

    with open(infile, 'rb') as imgfile:
        img = Image.open(imgfile)

        img = img.filter(ImageFilter.GaussianBlur(blurSize))
        if mode > 0:
            img = img.filter(ImageFilter.ModeFilter(mode))

    if preview:
        print("Preview Only")
        img.show()
    else:
        print(f"To: {new_filename}")
        img.save(new_filename)
