## 大目标：
- 权限

- stark组件

- crm业务

	---

	> [学习视频地址](https://www.bilibili.com/video/BV1vz411e7Yr)
	>
	> [老师博客](https://www.cnblogs.com/wupeiqi/articles/9178982.html)

	***

## 步骤：

#### 1.创建django project，luffy_permission

#### 2.两个app

- rbac，权限组件
- web，销售管理系统

#### 3.app：rbac

#### 4.app：web

#### 5.两个app的整合

#### 6.快速完成一个基本 权限控制，在 示例代码：

#### 7.功能的完善，将权限相关的功能放到rbac应用下，以便于以后组件的使用

总结：6/7属于进行权限控制

#### 8.动态菜单的功能

#### 9.点击非菜单权限时，默认选中或者默认展开

#### 10.路径导航

#### 11.权限粒度控制到按钮级别

总结：

> - 权限控制
>
> - 动态菜单
>
> - 权限的分配
>
>     问题：以前是如何做的权限分配？给某个用户分配以后角色？某个人分配某个权限。
>
>     答案：django admin进行录入

#### 12.权限分配

a. 角色管理

知识点:
> - ModelForm
> - 根据namespace和name 反向生成url
> - 模板的查找url顺序

b. 用户管理

知识点：

- ModelForm

> - 字段的自定制
> - 钩子方法
> - 错误提示（中文）
> - 重写__ init __方法,统一给所有字段添加属性（form-control）

- 根据namespace和name 反向生成url
- 模板的查找url顺序

c. 菜单和权限的增删改查

视频讲解：

> 一级
>
> 二级
>
> 权限

知识点：

>  保留原url的搜索条件
>
>  模板中int转换为str 1|safe
>
>  ModelForm定制 radio
>
>  ModelForm显示默认值
>
>  ModForm save之前对其它的instance进行修改
>
>  BootStrapModelForm基类

- e. 批量的权限操作

- f. 分配权限

