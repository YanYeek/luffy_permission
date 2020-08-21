from django.conf import settings


def init_permission(current_user, request):
	"""
	用户权限的初始化
	:param:current_user: 当前用户对象
	:param:request: 请求相关所有数据
	:return:
	"""
	# 2. 当前所有用户的权限
	permission_queryset = current_user.roles.filter(permissions__isnull=False).values('permissions__id',
	                                                                                  'permissions__title',
	                                                                                  'permissions__url',
	                                                                                  'permissions__pid',
	                                                                                  'permissions__menu_id',
	                                                                                  'permissions__menu__title',
	                                                                                  'permissions__menu__icon',
	                                                                                  ).distinct()
	
	# 3. 获取权限中的所有url+菜单信息
	# permission_list = [] # 由于较简单列表生成式
	# for item in permission_queryset:
	#     permission_list.append(item['permissions_url'])
	permission_list = []
	
	menu_dict = {}
	
	for item in permission_queryset:
		permission_list.append(
			{'id': item['permissions__id'], 'url': item['permissions__url'], 'pid': item['permissions__pid']})
		
		menu_id = item['permissions__menu_id']
		if not menu_id:
			continue

		node = {'id': item['permissions__id'], 'title': item['permissions__title'], 'url': item['permissions__url']}
		
		if menu_id in menu_dict:
			menu_dict[menu_id]['children'].append(node)

		else:
			menu_dict[menu_id] = {
				'title': item['permissions__menu__title'],
				'icon': item['permissions__menu__icon'],
				'children': [node, ]
			}

	# permission_list = [item['permissions__url'] for item in permission_queryset]
	
	# print(menu_dict)
	request.session[settings.PERMISSION_SESSION_KEY] = permission_list
	request.session[settings.MENU_SESSION_KEY] = menu_dict
