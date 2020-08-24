#!/usr/bin/env python
# encoding: utf-8
'''
@author: YanYeek
@file: urls.py
@time: 2020/8/23 22:26
@desc:
'''
from django.urls import reverse
from django.http import QueryDict


def memory_url(request, name, *args, **kwargs):
	"""
	生成带有原搜索条件的URL（替代了模板中的url方法）
	:param request:
	:param name:原路径
	:return:打包原参数为一个整体并返回
	"""
	basic_url = reverse(name, args=args, kwargs=kwargs)

	# 当前url中无参数
	if not request.GET:
		return basic_url

	query_dict = QueryDict(mutable=True)
	query_dict['_filter'] = request.GET.urlencode()  # 拿到参数字符串,并打包参数，用urlencode方法转义成整体

	return "%s?%s" % (basic_url, query_dict.urlencode())


def memory_reverse(request, name, *args, **kwargs):
	"""
	反向生成url
		http://127.0.0.1:8080/rbac/menu/add/?=_filter=mid%3D1
		1. 在俩中将原来搜索条件,如_filter后的值
		2. reverse生成原来的url，如/menu/list
		3. /menu/list?mid%3D1
	:param request:
	:param name:
	:param args:
	:param kwargs:
	:return:
	"""
	url = reverse(name, args=args, kwargs=kwargs)
	origin_params = request.GET.get('_filter')
	if origin_params:
		url = "%s?%s" % (url, origin_params)
	return url
