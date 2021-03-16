import os
import glob


def add_global_argments(sub_parser,
                        without_infile=False,
                        optional_outfile=True,
                        has_recursive=True,
                        has_overwrite=True,
                        has_preview=True):
    optional_header = '[Optional]' if optional_outfile else ''
    infile_tailer = ' or directory' if has_recursive else ' only'
    if not without_infile:
        sub_parser.add_argument('-i',
                                '--infile',
                                help=f"input file{infile_tailer}")

    sub_parser.add_argument('-o',
                            '--outfile',
                            help=f"{optional_header} the output file")

    if has_recursive:
        sub_parser.add_argument('-r',
                                '--recursive',
                                default=False,
                                action='store_true',
                                help='recursive the input dir, '
                                'outfiles will overwrite inputfiles. '
                                'And the -o will be ignore')
    if has_overwrite:
        sub_parser.add_argument('--overwrite',
                                action='store_false',
                                help='Overwrite the infile with new file')

    if has_preview:
        sub_parser.add_argument('-p',
                                '--preview',
                                action='store_true',
                                help='Show result directly with out save')


def parser_io_argments(params):
    infile = params['infile'] if 'infile' in params else None
    outfile = params['outfile'] if 'outfile' in params else None
    recursive = params['recursive'] if 'recursive' in params else None
    overwrite = params['overwrite'] if 'overwrite' in params else None
    preview = params['preview'] if 'preview' in params else None
    if infile and not os.path.exists(infile):
        print(f'Cant find --infile :{infile}')
        os._exit(1)

    if infile and os.path.isfile(infile) and recursive:
        print('"-r" is only for inputfile is a dir')
        os._exit(1)

    if infile and os.path.isdir(infile) and not recursive:
        print('"-r" is needed when --infile is a dir')
        os._exit(1)

    return infile, outfile, recursive, overwrite, preview


def get_recursive_pic_infiles(indir):
    file_exts = ['jpeg', 'jpg', 'png', 'webp', 'JPEG', 'JPG', 'PNG', 'WEBP']
    return get_recursive_infiles_by_ext(indir, file_exts)


def get_recursive_infiles_by_ext(indir, file_exts):
    paths = []
    for file_ext in file_exts:
        type_filter_str = os.path.join(
            f'{indir}', f'**/*.{file_ext}')
        picfiles = glob.glob(type_filter_str, recursive=True)
        paths.extend(picfiles)
    return paths


def auto_outfile(infile, postfix):
    filename, ext = os.path.splitext(infile)
    return f"{filename}{postfix}{ext}"
