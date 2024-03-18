from django.db import models


# Create your models here.
# 在此处编写数据模型代码
# 员工数据模型（员工数据表）
class employee(models.Model):
    # 员工姓名
    name = models.CharField(max_length=32, verbose_name='姓名')
    # 员工邮箱
    email = models.EmailField(verbose_name='邮箱')
    # 员工部门，外键，形成一对多的关系
    # ForeignKey类型，与department表中记录多对一关系
    # on_delete=models.CASCADE表示如果外键所关联的department表中的一条记录被删除，则本表中与这条记录有关联的记录将全部删掉
    dep = models.ForeignKey(to='department', on_delete=models.CASCADE)
    # 员工加入的团体，多对多关系，即一个员工可以加入多个团体，一个团体有多个员工
    group = models.ManyToManyField(to='group')
    # 薪水，数值类型
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    # 员工补充信息，一对一关系
    info = models.OneToOneField(to='employee_info', on_delete=models.CASCADE, null=True)


# 部门数据模型（部门数据表）
class department(models.Model):
    # 部门名称
    dep_name = models.CharField(max_length=32, verbose_name='部门名称')
    # 部门备注
    dep_script = models.CharField(max_length=60, verbose_name='部门备注')


# 团体数据模型（团体数据表）
class group(models.Model):
    # 团体名称
    group_name = models.CharField(max_length=32, verbose_name='团体名称')
    # 团体备注
    group_script = models.CharField(max_length=60, verbose_name='团体备注')


# 员工补充信息模型（员工补充信息数据表）
class employee_info(models.Model):
    # 电话号码
    phone = models.CharField(max_length=11)
    # 地址
    address = models.CharField(max_length=50)
