import os
import django

# 在environ字典里设置默认Django环境，'xxx.settings'指Django项目的配置文件
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_orm.settings')
django.setup()
from employee.models import *
from employee import models

# 正向操作查询字段名，取得字段值的形式为“外键+双下划线+关联表的字段名”
# values_list()返回元组（有字段值组成）列表
emp = employee.objects.values_list('name', 'dep__dep_name', 'dep__dep_script')
print(emp)
'''
<QuerySet
[('张三', '资产管理中心', '资产管理'), ('李四', '非结构部', '干涉发快递几个人'),
('王五', '你好部', '辅导机构鸿特'), ('赵六', '经营部', '经营、考核'),
('孙七', '放得部', '从基础福德宫'), ('姚八', '放得部', '从基础福德宫'),
('钱九', '经营部', '经营、考核'), ('周十', '存附部', '单据后温度计')]>
'''
# values()返回的值是字典列表，列表每一项为字典值、键名是字段名、值为字段值
emp2 = employee.objects.values('name', 'dep__dep_name', 'dep__dep_script')
print(emp2)
'''
<QuerySet 
[{'name': '张三', 'dep__dep_name': '资产管理中心', 'dep__dep_script': '资产管理'}, 
{'name': '李四', 'dep__dep_name': '非结构部', 'dep__dep_script': '干涉发快递几个人'}, 
{'name': '王五', 'dep__dep_name': '你好部', 'dep__dep_script': '辅导机构鸿特'}, 
{'name': '赵六', 'dep__dep_name': '经营部', 'dep__dep_script': '经营、考核'}, 
{'name': '孙七', 'dep__dep_name': '放得部', 'dep__dep_script': '从基础福德宫'}, 
{'name': '姚八', 'dep__dep_name': '放得部', 'dep__dep_script': '从基础福德宫'}, 
{'name': '钱九', 'dep__dep_name': '经营部', 'dep__dep_script': '经营、考核'}, 
{'name': '周十', 'dep__dep_name': '存附部', 'dep__dep_script': '单据后温度计'}]>
'''

# 反向操作查询字段名，取得字段值的形式为“表名+双下划线+字段名”
# 返回一个元组（由字段值组成）列表
dep_emp = models.department.objects.values_list("employee__name", "employee__email")
print(dep_emp)
'''
<QuerySet 
[('赵六', 'zhaoliu@163.com'), 
('钱九', 'qianjiu@163.com'), 
('张三', 'zhangsan@163.com')'
...(remaining elements truncated)...']>
'''
