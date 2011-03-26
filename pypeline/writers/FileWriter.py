# -*- coding: UTF8 -*-
from pypeline.writers import Writer

class FileWriter(Writer):
    def __call__(self, content):
        open(self.sink).write(content)
