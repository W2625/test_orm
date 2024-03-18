from django.urls import path, include
from employee.views import *

urlpatterns = [
    # path()中的两个参数中一个用来匹配路径，被称为URL表达式，它匹配网址的方式类似于正则表达式；
    # 另一个参数是视图函数名，视图函数在views.py中定义
    # 操作部门数据表（department）相关URL配置项
    path('list_dep_old/', list_dep_old),
    path('add_dep_old/', add_dep_old),
    path('edit_dep_old/<int:dep_id>/', edit_dep_old),
    # int指明数据类型
    path('del_dep_old/<int:dep_id>/', del_dep_old),
    # 操作团体数据表（group）相关URL配置项
    path('list_group_old/', list_group_old),
    path('add_group_old/', add_group_old),
    path('edit_group_old/<int:group_id>/', edit_group_old),
    path('del_group_old/<int:group_id>/', del_group_old),
    # 操作员工数据表（employee）相关URL配置项
    path('list_emp_old/', list_employee_old),
    path('add_emp_old/', add_employee_old),
    path('edit_emp_old/<int:emp_id>/', edit_employee_old),
    path('del_emp_old/<int:emp_id>/', del_employee_old),

    # 操作员工补充信息数据表（employee_info）相关URL配置项
    path('list_empinfo_old/', list_employeeinfo_old),
    path('add_empinfo_old/', add_employeeinfo_old),
    path('edit_empinfo_old/<int:info_id>/', edit_employeeinfo_old),
    path('del_empinfo_old/<int:info_id>/', del_employeeinfo_old),

    # 外键跨表关联操作实例
    path('test_foreign/', test_foreign),
]
