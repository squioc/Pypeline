# -*- coding: utf-8 -*-
from pypeline import Source

class Reader(Source):
    def __init__(self, source):
        self.source = source

    def __call__(self):
        pass

