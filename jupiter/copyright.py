"""A copyright utility"""

import datetime
import argparse

# def _get_file_type(file_name):
#     return file_name.split('.')[-1]
# 
class Doc:
    _file_type = ['c', 'cpp', 'py']
    _declaration = "Copyright (C) {0} {1}, all rights reserved."
    _formaters = {}

    def _get_file_type(file_name):
        return file_name.split('.')[-1]

    def __init__(self, file_name, author):
        self.file_name = file_name 
        self.author = author 
        self.file_type = Doc._get_file_type(self.file_name)
        self.declaration = Doc._declaration.format(datetime.date.today().year,
                self.author)

    def _c_cpp_formater(self):
        return "/* " + self.declaration + " */"
    _formaters['c'] = _c_cpp_formater
    _formaters['cpp'] = _c_cpp_formater
    _formaters['h'] = _c_cpp_formater

    def _py_formater(self):
        return "# " + self.declaration 
    _formaters['py'] = _py_formater

    def Get(self):
        return Doc._formaters[self.file_type](self)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file_name')
    parser.add_argument('-a', '--author', default="F.S.") 
    opt = parser.parse_args()
    print(Doc(opt.file_name, opt.author).Get())
