from django.urls import path
# 导入视图函数所在文件views.py，文件在当前目录
from . import views

urlpatterns = [
    path('hello_view/', views.hello_view),
    path('dep/<int:dep_id>/', views.depdetail, name='depdetail'),
    path('test_redirect/', views.test_redirect),
    # 因为基于类的通用视图函数在调用时以函数的形式而不能以类的形式被调用，需要把类视图转换为函数视图，所以在第二个参数（即类视图）后加“.as_view()”
    path('test_templateview/', views.test_templateview.as_view()),
    path('test_listview/', views.test_listview.as_view()),
    path('listviewdemo/', views.listviewdemo.as_view()),
    path('test_detailview/<int:personid>/', views.test_detailview.as_view()),
    path('detailviewdemo/<int:personid>/', views.detailviewdemo.as_view()),
]
