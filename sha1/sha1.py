# -*- coding: utf-8 -*-
import hashlib

class Sha1(object):

    def __init__(self, password):
        self.password = password
        self.password_sha1 = self.__convert_sha1(self)

    def __convert_sha1(self):
        
