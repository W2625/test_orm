import os
import django

# 在environ字典里设置默认Django环境，'xxx.settings'指Django项目的配置文件
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_orm.settings')
django.setup()

from employee import models

# # create()函数，创建一个新的记录并保存在数据库表中，最后将它添加到关联对象集（记录集）中
# # 正向操作
# models.employee.objects.first().group.create(group_name='搏击', group_script='搏击也是健身项目')
# # 反向操作
# models.group.objects.first().employee_set.create(name='tom', email='tom@163.com', salary='6600', dep_id='11')
# models.group.objects.get(id=13).employee_set.create(name='john', email='john@163.com', salary='5300', dep_id='11')
#
# # add()函数取出数据库表中的记录，然后将其添加到关联数据表的记录集
# group_list = models.group.objects.filter(id__lt=8)
# models.employee.objects.get(id=8).group.add(*group_list)
# # 把group中id值为14、15、16的记录关联到employee表的第9条记录上，注意列表钱要加“*”好
# models.employee.objects.get(id=9).group.add(*[14, 15, 16])
# # set()函数，更改数据库表中记录的关联关系，不管该记录以前关联任何记录，用新的关联替换
# models.employee.objects.get(id=14).group.set([8, 9, 12])
# # remove()函数，从记录对象中删除一条关联记录，参数为关联数据库表的id
# obj_list = models.employee.objects.all().first()
# obj_list.group.remove(12)
# # clear()函数，从记录对象中删去一切关联记录
# models.employee.objects.first().group.clear()


# 正向操作查询字段值，取得字段值的形式为“多对多键+双下划线+关联表的字段名”
# values_list()返回值为元组格式；如果一条记录关联多个值，这条记录将形成多条元组
emp_m2m = models.employee.objects.values_list("id", 'name', 'group__group_name')
print(emp_m2m)
'''
<QuerySet 
[(1, '张三', '等奖'), (2, '李四', '航次三等奖'), (3, '王五', '放的歌'), (4, '赵六', '付款后管理'), 
(8, '孙七', '航次三等奖'), (8, '孙七', '放的歌'), (9, '姚八', '航次三等奖'), (9, '姚八', '广佛'), 
(9, '姚八', '等奖'), (9, '姚八', '待付款赶紧哦'), (11, '钱九', '航次三等奖'), (12, '周十', '等奖'), 
(13, 'tom', '航次三等奖'), (14, 'john', '放的歌'), (14, 'john', '方式和'), (14, 'john', '费基尔')]>
'''
# 反向操作查询字段名，取得字段值的形式为“表名+双下划线+字段名”，表名用的是存在多对多键字段的表的名称
# values()返回字典类型
emp2_m2m = models.group.objects.values("group_name", "employee__name", "employee__email")
print(emp2_m2m)
'''
<QuerySet 
[{'group_name': '航次三等奖', 'employee__name': '李四', 'employee__email': 'lisi@163.com'}, 
{'group_name': '航次三等奖', 'employee__name': '姚八', 'employee__email': 'yaoba@163.com'}, 
{'group_name': '航次三等奖', 'employee__name': '钱九', 'employee__email': 'qianjiu@163.com'}, 
{'group_name': '航次三等奖', 'employee__name': 'tom', 'employee__email': 'tom@163.com'}, 
{'group_name': '航次三等奖', 'employee__name': '孙七', 'employee__email': 'sunqi@163.com'}, 
{'group_name': '放的歌', 'employee__name': '王五', 'employee__email': 'wangwu@163.com'}, 
{'group_name': '放的歌', 'employee__name': '孙七', 'employee__email': 'sunqi@163.com'}, 
{'group_name': '放的歌', 'employee__name': 'john', 'employee__email': 'john@163.com'}, 
{'group_name': '方式和', 'employee__name': 'john', 'employee__email': 'john@163.com'}, 
{'group_name': '费基尔', 'employee__name': 'john', 'employee__email': 'john@163.com'}, 
{'group_name': '付款后管理', 'employee__name': '赵六', 'employee__email': 'zhaoliu@163.com'}, 
{'group_name': '广佛', 'employee__name': '姚八', 'employee__email': 'yaoba@163.com'}, 
{'group_name': '等奖', 'employee__name': '周十', 'employee__email': 'zhoushi@163.com'}, 
{'group_name': '等奖', 'employee__name': '姚八', 'employee__email': 'yaoba@163.com'}, 
{'group_name': '等奖', 'employee__name': '张三', 'employee__email': 'zhangsan@163.com'}, 
{'group_name': '待付款赶紧哦', 'employee__name': '姚八', 'employee__email': 'yaoba@163.com'}, 
{'group_name': '德国黑', 'employee__name': None, 'employee__email': None}, 
{'group_name': '搏击', 'employee__name': None, 'employee__email': None}]>
'''
