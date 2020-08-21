import re
from django.shortcuts import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings


class RbacMiddleware(MiddlewareMixin):
	"""
		用户权限信息校验
	"""

	@staticmethod
	def process_request(request):
		"""
			当用户请求刚进入时触发执行
			:param request:
			:return:
		"""
		"""
			1. 获取当前用户请求url
			2. 获取当前用户在session中保存的权限列表 ['/customer/list/', ]
			3. 权限信息匹配
		"""

		current_url = request.path_info

		for valid_url in settings.VALID_URL_LIST:
			# if valid_url == current_url:
			if re.match(valid_url, current_url):
				# 白名单中的url无需权限验证即可访问
				return None  # 中间件返回None就表示不拦截

		permission_list = request.session.get(settings.PERMISSION_SESSION_KEY)
		if not permission_list:
			return HttpResponse('未获取到用户权限信息，请登录！')

		flag = False

		url_record = [
			{'title': '首页', 'url': '#'}
		]

		for item in permission_list:
			reg = "^%s$" % item['url']
			if re.match(reg, current_url):
				flag = True
				request.current_selected_permission = item['pid'] or item['id']
				if not item['pid']:
					url_record.extend([{'title': item['title'], 'url': item['url'], 'class': 'active'}])
				else:
					url_record.extend([
						{'title': item['p_title'], 'url': item['p_url']},
						{'title': item['title'], 'url': item['url'], 'class': 'active'},
					])
				request.breadcrumb = url_record

				break

		if not flag:
			return HttpResponse('无权访问')
