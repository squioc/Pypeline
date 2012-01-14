# -*- coding: UTF8 -*-
from urllib2 import urlopen, Request
from pypeline.readers import Reader

class HttpReader(Reader):
    def __init__(self, source, data = None, headers = dict()):
        self.source = source
        self.data = data
        self.headers = headers

    def __call__(self):
        yield urlopen(Request(self.source, data = self.data, headers = self.headers)).read()
