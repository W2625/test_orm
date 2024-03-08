import os
import django

# 在environ字典里设置默认Django环境，'xxx.settings'指Django项目的配置文件
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_orm.settings')
django.setup()

from employee import models
# 导入聚合函数相关模块
from django.db.models import Sum, Avg, Max, Min, Count

# 取得salary字段值并求合计值，字段名要包含在引号内
# 第一部分实现id值小于5的记录的查询，第二部分通过聚合函数Sum()把查询到的所有记录的salary字段值加到一起
salary_sum = models.employee.objects.filter(id__lt=5).aggregate(Sum("salary"))
print(salary_sum)
'''
聚合查询返回一个包含一些键值对的字典，即“字段名+双下划线+聚合函数”
{'salary__sum': Decimal('18304.00')}
'''
# 为聚合函数返回的字典的键指定一个名称
salary_sum = models.employee.objects.filter(id__lt=5).aggregate(salary_hj=Sum("salary"))
print(salary_sum)
'''
{'salary_hj': Decimal('18304.00')}
'''
# 生成多个聚合查询值，返回值为字典类型
salary_data = models.employee.objects.filter(id__lt=5).aggregate(count=Count("id"), salary_hj=Sum("salary"),
                                                                 salary_pj=Avg("salary"), salary_zd=Max("salary"),
                                                                 salary_zx=Min("salary"))
print(salary_data)
'''
{'count': 4, 'salary_hj': Decimal('18304.00'), 'salary_pj': 4576.0, 'salary_zd': Decimal('7512.00'), 'salary_zx': Decimal('2792.00')}
'''
