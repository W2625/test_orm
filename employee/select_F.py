import os
import django

# 在environ字典里设置默认Django环境，'xxx.settings'指Django项目的配置文件
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_orm.settings')
django.setup()

from employee import models
from django.db.models import F

# 实现id值小于5的员工的薪水增加600的功能
# 传到F函数中的字段名要用引号括起来
models.employee.objects.filter(id__lt=5).update(salary=F("salary") + 600)
