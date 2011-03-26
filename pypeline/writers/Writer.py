# -*- coding: UTF8 -*-
from pypeline import Sink

class Writer(Sink):
    def __init__(self, sink):
        self.sink = sink

    def __call__(self, content):
        pass

