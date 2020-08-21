import re
from collections import OrderedDict

from django.template import Library

from django.conf import settings

register = Library()


@register.inclusion_tag('rbac/static_menu.html')
def static_menu(request):
	"""
	创建一级菜单
	:return:
	"""
	menu_list = request.session[settings.MENU_SESSION_KEY]
	return {"menu_list": menu_list, 'request': request}


@register.inclusion_tag('rbac/multi_menu.html')
def multi_menu(request):
	"""
	创建二级菜单
	:return:
	"""
	"""
	{
		1: {'title': '信息管理',
			'icon': 'fa-fire',
			'children': [
				{'title': '客户列表','url': '/customer/list/'}
			]
		},
		2: {'title': '用户管理',
			'icon': 'fa-camera-retro',
			'children': [
				{'title': '账单列表', 'url': '/payment/list/'}
			]
		}
	}
	"""
	menu_dict = request.session[settings.MENU_SESSION_KEY]

	# 对字典的key进行排序
	key_list = sorted(menu_dict)
	# 空的有序字典
	ordered_dict = OrderedDict()
	
	for key in key_list:
		val = menu_dict[key]
		val['class'] = 'hide'
		
		for per in val['children']:
			if per['id'] == request.current_selected_permission:
				per['class'] = 'active'
				val['class'] = ''
		ordered_dict[key] = val

	return {"menu_dict": ordered_dict, 'request': request}
