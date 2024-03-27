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


# 用户登录数据模型
class loguser(models.Model):
    account = models.CharField(max_length=32, verbose_name='登录账号')
    password = models.CharField(max_length=20, verbose_name='密码')


# 用户信息数据模型
class person(models.Model):
    # 姓名
    name = models.CharField(max_length=32, verbose_name='姓名')
    # 邮箱
    email = models.EmailField(verbose_name='邮箱')
    # 性别，通过choices限定字段取值范围
    gender = models.CharField(max_length=1, choices=(('1', '男'), ('2', '女'),), verbose_name='性别')
    # 头像，upload_to指定图片上传的途径，如果不存在则自动创建
    head_img = models.ImageField(upload_to='headimage', blank=True, null=True, verbose_name='头像')
    # 附件，文件类型字段
    attachment = models.FileField(upload_to='filedir', blank=True, null=True, verbose_name='附件')
