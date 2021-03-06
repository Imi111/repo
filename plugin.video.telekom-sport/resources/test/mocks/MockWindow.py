# -*- coding: utf-8 -*-
# Module: Cache
# Author: asciidisco
# Created on: 24.07.2017
# License: MIT https://goo.gl/xF5sC4

"""Mock for Kodi Window instance"""

try:
    import cPickle as pickle
except ImportError:
    import pickle


class MockWindow(object):
    """Mock for Kodi Window instance"""

    def __init__(self):
        """ADD ME"""
        self.storage = {}

    def getProperty(self, name):
        """ADD ME"""
        return self.storage.get(name, pickle.dumps({}))

    def setProperty(self, name, value):
        """ADD ME"""
        self.storage[name] = value
