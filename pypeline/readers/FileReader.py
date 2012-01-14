# -*- coding: UTF8 -*-
import os
from pypeline.readers import Reader

class FileReader(Reader):
    def __init__(self, source):
        self.source = source

    def __call__(self):
        yield open(self.source).read()

