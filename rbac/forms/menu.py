#!/usr/bin/env python
# encoding: utf-8
'''
@author: YanYeek
@file: menu.py
@time: 2020/8/23 20:53
@desc:
'''
from django import forms
from django.utils.safestring import mark_safe
from rbac import models


class MenuModelForm(forms.ModelForm):
	class Meta:
		model = models.Menu
		fields = {'title', 'icon'}
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'icon': forms.RadioSelect(
				choices=[
					['fa-file-zip-o', mark_safe('<i class="fa fa-file-zip-o" aria-hidden="true"></i>')],
					['fa-gear', mark_safe('<i class="fa fa-gear" aria-hidden="true"></i>')],
				]
			)
		}
