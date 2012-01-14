# -*- coding: UTF8 -*-
import sys
from pypeline.readers import Reader

class ConsoleReader(Reader):
    def __call__(self):
        yield sys.stdin.read()
