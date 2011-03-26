# -*- coding: UTF8 -*-
from urllib2 import urlopen, Request
from pypeline.writers import Writer

class HttpWriter(Writer):
    def __init__(self, sink, headers=dict()):
        Writer.__init__(self, sink)
        self.headers = headers

    def __call__(self, content):
        urlopen(Request(self.sink, data = content, headers = self.headers))
