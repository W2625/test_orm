import os
import django

# 在environ字典里设置默认Django环境，'xxx.settings'指Django项目的配置文件
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_orm.settings')
django.setup()

from employee import models
from django.db.models import Count, Max, Avg

# 查询语句不含values()函数
# 统计每个员工参加的团体个数
# 得到employee中所有的记录，n个员工即n个组，每一组再有annotate()中的聚合函数进行分组
emp_list = models.employee.objects.annotate(groupnum=Count("group"))
for emp in emp_list:
    print(emp.name, "：参加", emp.groupnum, "个团体")
'''
张三 ：参加 1 个团体
李四 ：参加 1 个团体
王五 ：参加 1 个团体
赵六 ：参加 1 个团体
孙七 ：参加 2 个团体
姚八 ：参加 4 个团体
钱九 ：参加 1 个团体
周十 ：参加 1 个团体
tom ：参加 1 个团体
john ：参加 3 个团体
'''

# 统计每一个部门薪水最高值
# 第一种，Max("employee__salary")通过双下划线取得关联表的字段值
dep_list = models.department.objects.annotate(maxsalary=Max("employee__salary"))
for dep in dep_list:
    print(dep.dep_name, dep.maxsalary)
'''
经营部 4790.00 资产管理中心 5000.00  审计部 None    会饿部 None    打谷部 None    存附部 10000.00    电饭部 None
可促进部 None   非结构部 7512.00    你好部 3000.00 通过可以部 6600.00   提款机还让他部 None    地方锯部 None
不能发部 None   大放部 None    放得部 8000.00 奋达部 None    哎呀部 None    哈哈部 None    打客服部 None   读第部 None
'''
# 第二种，Max("employee__salary")通过双下划线取得关联表的字段值
dep_list = models.department.objects.annotate(maxsalary=Max("employee__salary")).values_list("dep_name", "maxsalary")
for dep in dep_list:
    print(dep)
'''
('经营部', Decimal('4790.00')) ('资产管理中心', Decimal('5000.00'))  ('审计部', None)   ('会饿部', None)   ('打谷部', None)
('存附部', Decimal('10000.00'))    ('电饭部', None)   ('可促进部', None)  ('非结构部', Decimal('7512.00'))
('你好部', Decimal('3000.00')) ('通过可以部', Decimal('6600.00'))   ('提款机还让他部', None)   ('地方锯部', None)  ('不能发部', None)
('大放部', None)   ('放得部', Decimal('8000.00')) ('奋达部', None)   ('哎呀部', None)   ('哈哈部', None)   ('打客服部', None)  ('读第部', None)
'''

# 查询语句包含values()函数
# values("dep")即以dep值分组字段，相当于SQL中group by dep；annotate()执行分组
# 计算每个部门员工的平均工资
dep_salary = models.employee.objects.values("dep").annotate(avg=Avg("salary")).values("dep__dep_name", "avg")
print(dep_salary)
'''
<QuerySet 
[{'dep__dep_name': '资产管理中心', 'avg': 5000.0}, {'dep__dep_name': '非结构部', 'avg': 7512.0}, 
{'dep__dep_name': '你好部', 'avg': 3000.0}, {'dep__dep_name': '经营部', 'avg': 3791.0}, 
{'dep__dep_name': '放得部', 'avg': 7200.0}, {'dep__dep_name': '存附部', 'avg': 10000.0}, 
{'dep__dep_name': '通过可以部', 'avg': 5950.0}]>
'''
