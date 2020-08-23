#!/usr/bin/env python
# encoding: utf-8
'''
@author: YanYeek
@file: role.py
@time: 2020/8/23 14:59
@desc:
'''
from django import forms
from rbac import models


class RoleModelForm(forms.ModelForm):
	class Meta:
		model = models.Role
		fields = ['title', ]
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'})
		}
