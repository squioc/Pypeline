# -*- coding: UTF8 -*-

class Pypeline(object):
    def __init__(self, reader, writer, transformers = list()):
        self.reader = reader
        self.writer = writer
        self.transformers = transformers

    def __call__(self):
        content = self.reader()
        for transformer in self.transformers:
            content = transformer(content)
        self.writer(content)

class Source(object):
    pass

class Sink(object):
    pass

class Tranformer(object):
    pass
