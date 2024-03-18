from django.shortcuts import render, HttpResponse

# Create your views here.

# 导入时间模块
import datetime


def hello_view(request):
    # 取出当前时间
    vnow = datetime.datetime.now().date()
    # 组合一个HTML格式的文本
    rep = "<div align='center'><h1>你好，欢迎你浏览本页面<h1/><hr>当前日期是%s<div/>" % vnow
    # 通过HttpResponse()函数返回一个HttpResponse对象
    # HttpResponse()函数把传给它的文本解析成HTML格式发送给网页
    return HttpResponse(rep)
