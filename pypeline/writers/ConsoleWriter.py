# -*- coding: UTF8 -*-
import sys
from pypeline.writers import Writer

class ConsoleWriter(Writer):
    def __call__(self, content):
        sys.stdout.write(content)
