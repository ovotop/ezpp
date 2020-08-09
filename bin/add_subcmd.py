#!/usr/bin/env python3
import sys
import os
from ezutils.files import readlines, writelines


def brother_path(filename): return os.path.join(
    os.path.dirname(__file__), filename)


def print_using():
    print('USING:')
    print('\tbin/add_subcmd.py [sub_cmd_name]')


def gen_subcmd_file(sub_cmd):
    m4cmd = f"define(`__SUB_CMD__', `{sub_cmd}')dnl"
    m4file_lines = readlines(brother_path('sub_cmd.py.m4'))
    m4file_lines.insert(0, m4cmd)
    writelines(m4file_lines, f'bin/{sub_cmd}.py.in')
    m4codes = '\n'.join(m4file_lines)
    # writelines([m4codes], f'bin/{sub_cmd}.py.in2')
    gen_cmd = f"{m4codes} | m4 > ezpp/{sub_cmd}.py"
    gen_cmd = f"m4 bin/{sub_cmd}.py.in > ezpp/{sub_cmd}.py && rm bin/{sub_cmd}.py.in"
    os.system(gen_cmd)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_using()
        exit(1)

    sub_cmd = sys.argv[1]
    gen_subcmd_file(sub_cmd)
