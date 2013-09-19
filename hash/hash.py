# -*- coding: utf-8 -*-
import hashlib

SALT = 'AAABBBCCC'


class Hash(object):
    '''ハッシュクラス'''

    def __init__(self, hash_name, password):
        self.hash_name = hash_name
        self.password = password
        self.hash = self.__execute_hash(self)

    def __execute_hash(self):
        h = hashlib.new(self.hash_name)
        h.update(self.password + SALT)
        return h.hexdigest()
