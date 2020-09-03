# Copyright (C) 2020 Francis Sun, all rights reserved.

import os


def get_include_guard(header_path, prefix=None):
    # rm beginning os.sep
    if header_path[0] == os.sep:
        header_path = header_path[1:]
    # rm insignificant beginning word, e.g. src, test
    header_path_parts = header_path.split(os.sep)
    first_part = header_path_parts[0]
    insignificant_beginning_word = ['src', 'test']
    for w in insignificant_beginning_word:
        if first_part == w:
            header_path = header_path[len(w) + 1:]

    header_path = header_path.replace(os.sep, '_')
    header_path = header_path.replace('.', '_')
    if prefix:
        header_path = prefix + '_' + header_path
    header_path = header_path.upper()

    return ['#ifndef ' + header_path,
            '#define ' + header_path,
            '#endif // ' + header_path]
