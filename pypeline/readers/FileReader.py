# -*- coding: UTF8 -*-
import os
from pypeline.readers import Reader

class FileReader(Reader):
    def __call__(self):
        return open(self.source).read()

