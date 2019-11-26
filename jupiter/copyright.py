"""A copyright utility"""

import datetime

class Doc:
    _file_type = ['c', 'cpp', 'py']
    _declaration = "Copyright (C) {0} {1}, all rights reserved"
    _formaters = {}
    def __init__(info):
        self.author = info['author']
        self.file_type = info['file_type']
        self.declaration = _declaration.format(datetime.date.today().year,
                self.author)

    def _c_cpp_formater():
        return "/* " + self.declaration + " */"
    _formaters['c'] = _c_cpp_formater
    _formaters['cpp'] = _c_cpp_formater

    def _py_formater():
        return "# " + self.declaration 
    _formaters['py'] = _py_formater

    def Get():
        return _formaters[self.file_type]()
