# -*- coding: utf-8 -*-
from django.db import models


class Users(models.Model):
    username = models.CharField(u"ユーザ名", max_length=255)
    email = models.CharField(u"メールアドレス", max_length=75)
    password = models.CharField(u"パスワード", max_length=255)
    date_joined = models.DateTimeField(u"登録日", auto_now=True, null=False)
    last_login = models.DateTimeField(u"最終ログイン日", auto_now=True, null=False)

    class Meta:
        db_table = "users"

    def __init__(self, id, password):
        self.id = id
        self.password = password

    def get_user_by_id(self):
        '''IDで取得'''
        try:
            m = Users.objects.get(id__exact=self.id)
        except:
            m = None

        if m:
            return m

        return None

    def set_user(self):
        '''IDで取得'''
        try:
            m = Users.objects.create(id=self.id, password=self.password)
        except:
            m = None

        if m:
            return m

        return None
