# -*- coding: utf-8 -*-


class Session(object):

    def __init__(self, request, user):
        self.request = request
        self.user = user
        self.request.session['user_id'] = self.user.id

    @classmethod
    def check_session(cls, request):
        if request.session.get('user_id'):
            return True
        return False

    def delete_session(self, key):
        del self.request.session[key]
        
    @classmethod
    def set_user_id(cls, request, user):
        request.session['user_id'] = user.id

    @classmethod
    def get_user_id(cls, request):
        user_id = request.session.get('user_id')
        if user_id:
            return user_id
        return False
