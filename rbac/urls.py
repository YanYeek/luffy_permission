#!/usr/bin/env python
# encoding: utf-8
'''
@author: YanYeek
@file: urls.py
@time: 2020/8/23 12:49
@desc:
'''
from django.conf.urls import url, include
from django.contrib import admin
from rbac.views import role

urlpatterns = [
	url(r'^role/list/$', role.role_list, name='role_list'),  # rbac:role_list
	url(r'^role/add/$', role.role_add, name='role_add'),  # rbac:role_add
	url(r'^role/edit/(?P<pk>\d+)/$', role.role_edit, name='role_edit'),  # rbac:role_edit
	url(r'^role/del/(?P<pk>\d+)/$', role.role_del, name='role_del'),  # rbac:role_del
]
