from django.db import models

# Create your models here.

# 导入反向解析函数
from django.urls import reverse


# 部门数据模型（部门数据表）
class department(models.Model):
    # 部门名称，字符类型
    dep_name = models.CharField(max_length=32, verbose_name='部门名称', unique=True, blank=False)
    # 部门备注说明
    dep_script = models.CharField(max_length=60, verbose_name='备注', null=True)

    # 数据模型的get_absolute_url()方法
    def get_absolute_url(self):
        # 反向解析URL，解析成/dep/ self.pk /
        return reverse('depdetail', kwargs={'dep_id': self.pk})
