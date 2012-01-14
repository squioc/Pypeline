# -*- coding: UTF8 -*-
from pypeline.writers import Writer

class FileWriter(Writer):
    def __init__(self, sink):
        self.sink = sink

    def __call__(self, content):
        open(self.sink, 'a+').write(content)
