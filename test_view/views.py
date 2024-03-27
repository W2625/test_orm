from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

# 导入时间模块
import datetime
from . import models


def hello_view(request):
    # 取出当前时间
    vnow = datetime.datetime.now().date()
    # 组合一个HTML格式的文本
    rep = "<div align='center'><h1>你好，欢迎你浏览本页面<h1/><hr>当前日期是%s<div/>" % vnow
    # 通过HttpResponse()函数返回一个HttpResponse对象
    # HttpResponse()函数把传给它的文本解析成HTML格式发送给网页
    return HttpResponse(rep)


def depdetail(request, dep_id):
    # 根据传入的参数值取出一条记录
    obj = models.department.objects.get(id=dep_id)
    # 返回HttpResponse对象
    return HttpResponse('部门：' + obj.dep_name + ',备注：' + obj.dep_script)


# # 方法一（参数是数据模型对象（Model）时）
# def test_redirect(request):
#     obj = models.department.objects.get(id=1)
#     # 用redirect()重定向，参数是数据模型对象，所以重定向到数据模型get_absolute_url生成的URL
#     # 这个URL对应视图函数views.depdetail()，实际上调用这个函数
#     return redirect(obj)

# 方法二（参数是视图函数名称时）
def test_redirect(request):
    # 视图函数depdetail()有参数dep_id
    return redirect('depdetail', dep_id=2)


from django.views.generic import TemplateView


# 视图继承于TemplateView
class test_templateview(TemplateView):
    # 设置模版文件
    template_name = 'test_view/test_temp.html'

    # 重写父类get_context_data()方法
    def get_context_data(self, **kwargs):
        context = super(test_templateview, self).get_context_data(**kwargs)
        # 增加一个模版变量test
        context['test'] = '这是一个要传递的变量'
        return context


from django.views.generic import ListView


# 视图继承于ListView
class test_listview(ListView):
    # 设置数据模型
    model = models.department
    # 设置模版文件
    template_name = 'test_view/test_listview.html'
    # 设置模版变量，若无指定context_object_name默认使用object_list作为模版变量的名字
    context_object_name = 'person_list'


class listviewdemo(ListView):
    # 设置模版文件
    template_name = 'test_view/listviewdemo.html'
    # 设置模版变量，若无指定context_object_name默认使用object_list作为模版变量的名字
    context_object_name = 'person_list'

    # 重写get_queryset()取person中性别为女的人员，gender值为'2'
    def get_queryset(self):
        # 按照gender='2'过滤数据
        personlist = models.person.objects.filter(gender='2')
        return personlist

    # 重写父类的get_context_data()，增加模版变量loguser
    def get_context_data(self, **kwargs):
        kwargs['loguser'] = models.loguser.objects.all().first()
        # 继承父类模版变量的属性，并通过return语句返回这一模版变量（字典类型）
        return super(listviewdemo, self).get_context_data(**kwargs)
