# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from session.utile.base_utile import Session
from users.models import Users
from peapron.decorate import login_required
from hash_manager.hash_manager import HashManager


@login_required
def index(request):
    """mypage"""
    user = request.user
    rctxt = RequestContext(request, {
        "member": user,

    })

    return render_to_response(
        'index.html', "",
        context_instance=rctxt)


def login(request):
    """ログイン"""
    user = None
    if request.method == "POST":
        if request.POST["username"] and request.POST["password"]:
            user = Users.get_user(request.POST["username"],
                                  request.POST["password"])
            if user:
                Session.set_user_id(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        return render_to_response(
            'login_index.html', "",
            context_instance=RequestContext(request))

    return HttpResponseRedirect(reverse('login'))


'''password,idが正しいかチェックするデコレータほしい'''
def user_regist(request):
    """登録"""
    if request.method == "POST":
        h = HashManager('sha1', request.POST["password"])
        user = Users(request.POST["password"], h.password)
        if user:
            return HttpResponseRedirect(reverse('user_regist_complete'))

    else:
        return render_to_response(
            'user_regist_index.html', "",
            context_instance=RequestContext(request))
 
    return render_to_response(
        'user_regist_index.html', "",
        context_instance=RequestContext(request))
