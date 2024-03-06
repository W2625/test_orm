"""test_orm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 用include()函数把二级配置包含进来
    # include()函数中的参数是一个字符串，这个字符串指定二级URL配置文件的位置，
    # 与文件的路径有些相似，只是用“.”作为分隔符，并且最后的文件名不包含扩展名。
    # 如果URL配置文件分级，在匹配URL时，要把各级配置文件中URL表达式合并成一个完整的URL表达式进行匹配。
    path('test_orm_old/', include('employee.urls')),
]
