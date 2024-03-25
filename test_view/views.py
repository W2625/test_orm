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

# 方法一（参数是视图函数名称时）
def test_redirect(request):
    # 视图函数depdetail()有参数dep_id
    return redirect('depdetail', dep_id=2)
