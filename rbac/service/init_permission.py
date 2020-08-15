from django.conf import settings

def init_permission(current_user, request):
    """
    用户权限的初始化
    :param:current_user: 当前用户对象
    :param:request: 请求相关所有数据
    :return:
    """
    # 2. 当前所有用户的权限
    permission_queryset = current_user.roles.filter(permissions__isnull=False).all().values('permissions__id',
                                                                                            'permissions__title',
                                                                                            'permissions__url',
                                                                                            'permissions__menu_id',
                                                                                            'permissions__menu__title',
                                                                                            'permissions__menu__icon',
                                                                                            ).distinct()
    
    # 3. 获取权限中的所有url+菜单信息
    # permission_list = [] # 由于较简单列表生成式
    # for item in permission_queryset:
    #     permission_list.append(item['permissions_url'])
    menu_dict = {}
    permission_list = []
    for item in permission_queryset:
        permission_list.append(item['permissions__url'])
        
        menu_id = item['permissions__menu_id']
        if item['permissions__is_menu']:
            temp = {
                'title':item['permissions__title'],
                'icon':item['permissions__icon'],
                'url':item['permissions__url'],
            }
            menu_list.append(temp)
    
    # permission_list = [item['permissions__url'] for item in permission_queryset]
    
    
    request.session[settings.PERMISSION_SESSION_KEY] = permission_list
    request.session[settings.MENU_SESSION_KEY] = menu_list