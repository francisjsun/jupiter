"""A copyright utility"""

import datetime
import argparse
import os
import os.path


class Copyright:
    _unknown_file_type = "unknown file type"
    _file_type = {
            'c/c++': ['h', 'c', 'cpp', 'cc'],
            'python': ['py']}
    _declaration = "Copyright (C) {0} {1}, all rights reserved."
    _formaters = {}

    def __init__(self, file_path, author):
        self.file_path = file_path 
        self.author = author 
        self.file_type = self.file_path.split('.')[-1]
        self.declaration = Copyright._declaration.format(datetime.date.today().year, \
                self.author)

    def _c_cpp_formater(self):
        return "/* " + self.declaration + " */"
    for ft in _file_type['c/c++']:
        _formaters[ft] = _c_cpp_formater

    def _py_formater(self):
        return "# " + self.declaration 
    for ft in _file_type['python']:
        _formaters[ft] = _py_formater

    def Get(self):
        if self.file_type in Copyright._formaters:
            return Copyright._formaters[self.file_type](self)
        else:
            return Copyright._unknown_file_type + ": " + self.file_type + ", @file_path: " + \
                    self.file_path

    tmp_filename_suffix = ".fjcu"

    def Write(self):
        tmp_filename = self.file_path + Copyright.tmp_filename_suffix
        with open(tmp_filename, 'w') as tmp_f:
            origin_content = ""
            if os.path.isfile(self.file_path):
                with open(self.file_path, 'r') as origin_f:
                    origin_content = origin_f.read()
            tmp_f.write(self.Get() + "\n" + origin_content)
            os.replace(tmp_filename, self.file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file_path')
    parser.add_argument('-a', '--author', default="F.S.") 
    opt = parser.parse_args()
    cr = Copyright(opt.file_path, opt.author)
    cr.Write()

