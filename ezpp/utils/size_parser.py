#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def parse_position(parent_size: int, position_str: str) -> int:
    if position_str is None:
        return 0

    if not isinstance(position_str, str):
        print(f"type of position_str is {type(position_str)}")
        position_str = f"{position_str}"

    if position_str == "center":
        return int(parent_size/2)

    if position_str == "start":
        return 0

    if position_str == "end":
        return parent_size

    # 如果不是以上字符串，可能是数字，解析这个数字
    if position_str.isdigit():
        pos = int(position_str)
        print(f"pos is {pos}")
        return pos
    return 0
