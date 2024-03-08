# import os
# import django
#
# # 在environ字典里设置默认Django环境，'xxx.settings'指Django项目的配置文件
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_orm.settings')
# django.setup()
#
# from employee import models
#
# # 正向操作
# # emp = models.employee.objects.get(id=1)
# # phone = emp.info.phone
#
# # 反向操作第一种
# emp_info = models.employee_info.objects.get(id=2)
# # 因为定义了related_name="info_related"，所以用info_related
# emp_name = emp_info.info_related.name
# # 反向操作第二种
# # 如果在models.py的employee类中的info字段未定义related_name="info_related"
# # 一对一反向操作不用employee_set，直接employee
# emp_name = emp_info.employee.name
# print(emp_name)

import os
import django

# 在environ字典里设置默认Django环境，'xxx.settings'指Django项目的配置文件
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_orm.settings')
django.setup()

from employee import models

# 正向操作查询字段名，取得字段值的形式为“外键+双下划线+关联表的字段名”
# values()返回的值是字典列表，列表每一项为字典值、键名是字段名、值为字段值
emp_one = models.employee.objects.values("id", "name", "email", "info__phone", "info__address")
print(emp_one)
'''
<QuerySet 
[{'id': 1, 'name': '张三', 'email': 'zhangsan@163.com', 'info__phone': '14793568427', 'info__address': '山东科技飞机'}, 
{'id': 2, 'name': '李四', 'email': 'lisi@163.com', 'info__phone': '18672943851', 'info__address': '度还剩多少'}, 
{'id': 3, 'name': '王五', 'email': 'wangwu@163.com', 'info__phone': '13498939957', 'info__address': '今年淋巴大家庭'}, 
{'id': 4, 'name': '赵六', 'email': 'zhaoliu@163.com', 'info__phone': '16795234812', 'info__address': '付饿哦日几个'}, 
{'id': 8, 'name': '孙七', 'email': 'sunqi@163.com', 'info__phone': '16853247492', 'info__address': '车架号割肉'}, 
{'id': 9, 'name': '姚八', 'email': 'yaoba@163.com', 'info__phone': '17964853457', 'info__address': '就发货哦我甲方'}, 
{'id': 11, 'name': '钱九', 'email': 'qianjiu@163.com', 'info__phone': '16579542384', 'info__address': '成本金额开发出局本级荣威'}, 
{'id': 12, 'name': '周十', 'email': 'zhoushi@163.com', 'info__phone': '15623296564', 'info__address': '好好干大煞风景哦热个人'}, 
{'id': 13, 'name': 'tom', 'email': 'tom@163.com', 'info__phone': None, 'info__address': None}, 
{'id': 14, 'name': 'john', 'email': 'john@163.com', 'info__phone': None, 'info__address': None}]>
'''
# 反向操作查询字段名，取得字段值的形式为“表名+双下划线+字段名”
# values()返回的值是字典列表，列表每一项为字典值、键名是字段名、值为字段值
emp_one2 = models.employee_info.objects.values("phone", "address", "employee__name", "employee__email")
print(emp_one2)
'''
<QuerySet 
[{'phone': '15623296564', 'address': '好好干大煞风景哦热个人', 'employee__name': '周十', 'employee__email': 'zhoushi@163.com'}, 
{'phone': '13498939957', 'address': '今年淋巴大家庭', 'employee__name': '王五', 'employee__email': 'wangwu@163.com'}, 
{'phone': '14793568427', 'address': '山东科技飞机', 'employee__name': '张三', 'employee__email': 'zhangsan@163.com'}, 
{'phone': '16853247492', 'address': '车架号割肉', 'employee__name': '孙七', 'employee__email': 'sunqi@163.com'}, 
{'phone': '15879235874', 'address': '融和通', 'employee__name': None, 'employee__email': None}, 
{'phone': '18672943851', 'address': '度还剩多少', 'employee__name': '李四', 'employee__email': 'lisi@163.com'}, 
{'phone': '16795234812', 'address': '付饿哦日几个', 'employee__name': '赵六', 'employee__email': 'zhaoliu@163.com'}, 
{'phone': '17964853457', 'address': '就发货哦我甲方', 'employee__name': '姚八', 'employee__email': 'yaoba@163.com'}, 
{'phone': '15763249856', 'address': '多喝水氛围感', 'employee__name': None, 'employee__email': None}, 
{'phone': '16579542384', 'address': '成本金额开发出局本级荣威', 'employee__name': '钱九', 'employee__email': 'qianjiu@163.com'},
{'phone': '17546823647', 'address': '电话成本都是擦掉测地哦', 'employee__name': None, 'employee__email': None}]>
'''
