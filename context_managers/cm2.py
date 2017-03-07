#!/usr/bin/python

class File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.open(self.filename, self.filename)
        return self.

    def __exit__(self, *args):
        
