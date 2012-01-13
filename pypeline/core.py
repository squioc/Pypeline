# -*- coding: UTF8 -*-

from collections import Iterable

class Pypeline(object):
    def __init__(self, reader, writer, transformers = list()):
        self.reader = reader
        self.writer = writer
        self.transformers = transformers

    def __get_iter(self, obj):
        if isinstance(obj, Iterable):
            for element in obj:
                yield element
        else:
            yield obj

    def __call__(self):
        for content in self.__get_iter(self.reader()):
            for transformer in self.transformers:
                content = transformer(content)
            self.writer(content)

class Source(object):
    pass

class Sink(object):
    pass

class Tranformer(object):
    pass
