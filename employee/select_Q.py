import os
import django

# 在environ字典里设置默认Django环境，'xxx.settings'指Django项目的配置文件
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_orm.settings')
django.setup()

from employee import models
from django.db.models import Q

# “&”与（AND）关系、“|”或（OR）关系、“~”非/反（NOT）关系
# 在employee数据表中查询id值小于8或者salary值小于5000的记录
obj = models.employee.objects.filter(Q(id__lt=8) | Q(salary__lt=7000))
print(obj.values())
'''
<QuerySet 
[{'id': 1, 'name': '张三', 'email': 'zhangsan@163.com', 'dep_id': 2, 'salary': Decimal('6200.00'), 'info_id': 4}, 
{'id': 2, 'name': '李四', 'email': 'lisi@163.com', 'dep_id': 9, 'salary': Decimal('8712.00'), 'info_id': 10}, 
{'id': 3, 'name': '王五', 'email': 'wangwu@163.com', 'dep_id': 10, 'salary': Decimal('4200.00'), 'info_id': 2}, 
{'id': 4, 'name': '赵六', 'email': 'zhaoliu@163.com', 'dep_id': 1, 'salary': Decimal('3992.00'), 'info_id': 12}, 
{'id': 8, 'name': '孙七', 'email': 'sunqi@163.com', 'dep_id': 16, 'salary': Decimal('6400.00'), 'info_id': 5}, 
{'id': 11, 'name': '钱九', 'email': 'qianjiu@163.com', 'dep_id': 1, 'salary': Decimal('4790.00'), 'info_id': 16}, 
{'id': 13, 'name': 'tom', 'email': 'tom@163.com', 'dep_id': 11, 'salary': Decimal('6600.00'), 'info_id': None}, 
{'id': 14, 'name': 'john', 'email': 'john@163.com', 'dep_id': 11, 'salary': Decimal('5300.00'), 'info_id': None}]>
'''
# 在employee数据表中查询salary值大于5000并且name字段值开头不是“王”的记录
obj2 = models.employee.objects.filter(Q(salary__gt=7000) & ~ Q(name__startswith="王"))
print(obj2.values())
'''
<QuerySet [{'id': 2, 'name': '李四', 'email': 'lisi@163.com', 'dep_id': 9, 'salary': Decimal('8712.00'), 'info_id': 10}, 
{'id': 9, 'name': '姚八', 'email': 'yaoba@163.com', 'dep_id': 16, 'salary': Decimal('8000.00'), 'info_id': 13}, 
{'id': 12, 'name': '周十', 'email': 'zhoushi@163.com', 'dep_id': 6, 'salary': Decimal('10000.00'), 'info_id': 1}]>
'''

