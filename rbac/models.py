from django.db import models


class Menu(models.Model):
	title = models.CharField(verbose_name='一级菜单名称', max_length=32)
	icon = models.CharField(verbose_name="图标", max_length=32, null=True, blank=True)
	
	def __str__(self):
		return self.title


class Permission(models.Model):
	"""
	权限表
	"""
	title = models.CharField(verbose_name='标题', max_length=32)
	url = models.CharField(verbose_name='含正则的URL', max_length=128)
	
	menu = models.ForeignKey(verbose_name='所属菜单', to='Menu', null=True, blank=True, help_text='null表示不是菜单;非null表示是二级菜单')
	# is_menu = models.BooleanField(verbose_name="是否可以做菜单", default=False)
	# icon = models.CharField(verbose_name = "图标", max_length=32, null=True, blank=True)
	
	pid = models.ForeignKey(verbose_name='关联的权限', to='Permission', null=True, blank=True, related_name='parents',
	                        help_text='对于非菜单权限需要选择一个可以成为菜单的权限,用户做默认展开和选中菜单。')
	
	def __str__(self):
		return self.title


class Role(models.Model):
	"""
	角色
	"""
	title = models.CharField(verbose_name='角色名称', max_length=32)
	permissions = models.ManyToManyField(verbose_name='拥有的所有权限', to='Permission', blank=True)
	
	def __str__(self):
		return self.title


class UserInfo(models.Model):
	"""
	用户表
	"""
	name = models.CharField(verbose_name='用户名', max_length=32)
	password = models.CharField(verbose_name='密码', max_length=64)
	email = models.CharField(verbose_name='邮箱', max_length=32)
	roles = models.ManyToManyField(verbose_name='拥有的所有角色', to='Role', blank=True)
	
	def __str__(self):
		return self.name


"""
	current_user = models.UserInfo.objects.filter(name=user, password=pwd).first()
	# 获取当前用户所拥有的所有角色 select id,name,xx from xb 使用内部关联查询
	current_user.roles.filter(permissions__isnull=False).all().values('permissions__url').distinct()
	# 问题一：1.一个用户有多个角色 2.一个角色有多个权限 解决：去重
	# 问题二：角色的权限可能为空，需要排除这种情况
"""
