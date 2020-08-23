#!/usr/bin/env python
# encoding: utf-8
'''
@author: YanYeek
@file: role.py
@time: 2020/8/23 12:45
@desc:角色管理
'''
from django.urls import reverse
from django.shortcuts import render, redirect, HttpResponse

from rbac import models
from rbac.forms.role import RoleModelForm


def role_list(request):
	"""
	角色列表
	:param request:
	:return:
	"""
	role_queryset = models.Role.objects.all()

	return render(request, 'rbac/role_list.html', {'roles': role_queryset})


def role_add(request):
	"""
	添加角色
	:param request:
	:return:
	"""
	if request.method == 'GET':
		form = RoleModelForm()
		return render(request, 'rbac/change.html', {'form': form})

	form = RoleModelForm(data=request.POST)
	if form.is_valid():
		form.save()
		return redirect(reverse('rbac:role_list'))

	return render(request, 'rbac/change.html', {'form': form})


def role_edit(request, pk):
	"""
	编辑角色
	:param request:
	:param pk:要修改的角色id
	:return:
	"""
	obj = models.Role.objects.filter(id=pk).first()
	if not obj:
		return HttpResponse('角色不存在')
	if request.method == 'GET':
		form = RoleModelForm(instance=obj)
		return render(request, 'rbac/change.html', {'form': form})
	form = RoleModelForm(instance=obj, data=request.POST)
	if form.is_valid():
		form.save()
		return redirect(reverse('rbac:role_list'))

	return render(request, 'rbac/change.html', {'form': form})


def role_del(request, pk):
	"""
	删除角色
	:param request:
	:param pk:要删除的角色id
	:return:
	"""
	origin_url = reverse('rbac:role_list')
	if request.method == 'GET':
		return render(request, 'rbac/delete.html', {'cancel_url': origin_url})

	models.Role.objects.filter(id=pk).delete()

	return redirect(origin_url)
