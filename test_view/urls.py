from django.urls import path
# 导入视图函数所在文件views.py，文件在当前目录
from . import views

urlpatterns = [
    path('hello_view/', views.hello_view),
    path('dep/<int:dep_id>/', views.depdetail, name='depdetail'),
    path('test_redirect/', views.test_redirect),

]
