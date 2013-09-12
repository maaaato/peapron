# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import functools

from session.utile.base_utile import Session
from users.models import Users


def login_required(func):
    '''ログインチェック'''
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        request = args[0]  # requestを取得

        if not Session.check_session(request):
            return HttpResponseRedirect(reverse('login'))
        
        user_id = Session.get_user_id(request)
        if user_id:
            user = Users.get_user_by_id(user_id)
            request.user = user

        return func(*args, **kwargs)

    return wrapper
