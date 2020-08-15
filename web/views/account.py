from django.shortcuts import HttpResponse,render,redirect
from django.conf import settings
from rbac import models

from rbac.service.init_permission import init_permission

def login(request):
    # 1. 用户登录
    if request.method == 'GET':
        return render(request, 'login.html')
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')

    current_user = models.UserInfo.objects.filter(name=user, password=pwd).first()
    if not current_user:
        return render(request, 'login.html', {'msg':'用户名或密码错误'})
    
    # 根据当前用户信息获取到此用户所拥有的所有权限并放入session。

    # 2. 权限信息初始化
    init_permission(current_user, request)

    return redirect('/customer/list')