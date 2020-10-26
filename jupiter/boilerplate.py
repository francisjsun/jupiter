# Copyright (C) 2020 Francis Sun, all rights reserved.

import os
from .copyright_declaration import Copyright


def get_include_guard(header_path, macro_ignored_dir, prefix=None):
    # rm the beginning os.sep
    if header_path[0] == os.sep:
        header_path = header_path[1:]
    # rm insignificant beginning word, e.g. src, test
    for w in macro_ignored_dir:
        if header_path.startswith(w):
            header_path = header_path[len(w) + 1:]
            break

    header_path = header_path.replace(os.sep, '_')
    header_path = header_path.replace('.', '_')
    if prefix:
        header_path = prefix + '_' + header_path
    header_path = header_path.upper()

    return ['#ifndef ' + header_path,
            '#define ' + header_path,
            '#endif  // ' + header_path]


def get(abs_project_dir, rel_file_path, author, macro_ignored_dir, prefix):
    # rm the beginning os.sep
    if rel_file_path[0] == os.sep:
        rel_file_path = rel_file_path[1:]

    ret = {}
    cr = Copyright(rel_file_path, author)
    cr_d = cr.get_declaration()
    if cr_d:
        ret["copyright_declaration"] = cr_d

    e_r = rel_file_path.rsplit('.', maxsplit=1)
    file_path_root = e_r[0]
    file_path_ext = e_r[1]

    if file_path_ext == 'h':
        ret['include_guard'] = get_include_guard(
            rel_file_path, macro_ignored_dir, prefix)

    if file_path_ext == 'cpp' or file_path_ext == 'c' or file_path_ext == 'cc':
        # check if corresponding header file exists
        if os.path.isfile(os.path.join(abs_project_dir,
                                       file_path_root + '.h')):
            header_name = file_path_root.split(os.sep)[-1] + '.h'
            ret['cpp_include_header'] = "#include \"" + header_name + "\""

    return ret
