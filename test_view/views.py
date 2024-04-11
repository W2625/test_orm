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


from django.views.generic import DetailView


# 视图继承于DetailView
class test_detailview(DetailView):
    # 设置数据模型
    model = models.person
    # 设置模版文件
    template_name = 'test_view/test_detailview.html'
    # 设置模版变量
    context_object_name = 'person'
    # 在urls.py文件的urlpatterns定义的URL正则表达式中的实名参数personid
    pk_url_kwarg = 'personid'


class detailviewdemo(DetailView):
    model = models.person
    template_name = 'test_view/detailviewdemo.html'
    context_object_name = 'person'
    # 在urls.py文件的urlpatterns定义的URL正则表达式中的实名参数personid
    pk_url_kwarg = 'personid'

    def get_object(self, queryset=None):
        # 调用父类的get_object()
        obj = super(detailviewdemo, self).get_object()
        if obj.gender == '1':
            obj.gender = '男'
        else:
            obj.gender = '女'
        return obj

    def get_context_data(self, **kwargs):
        # 增加一个变量test
        kwargs['test'] = '这是一个DetailView类通用视图生成的页面'
        return super(detailviewdemo, self).get_context_data(**kwargs)


# ----------------------------------------------------------------------------------------------------------
# 实例4（Django视图应用开发）
def login(request):
    if request.method == 'POST':
        # 取得表单提交的account值
        account = request.POST.get('account')
        # 取得表单提交的password值
        password = request.POST.get('password')
        # 勾选了checkbox，get()取得的值是字符串on，未勾选则值是None
        remember = request.POST.get('remember')
        # 数据库查询用户
        loguser = models.loguser.objects.filter(account=account, password=password).first()
        if loguser:
            rep = redirect('/test_view/index/')
            if remember == 'on':
                rep.set_cookie('account', account, max_age=60 * 60 * 8)
            return rep
        else:
            errmsg = '用户名或密码错误'
            return render(request, 'test_view/login.html', {'errmsg': errmsg})
    # 第二个参数是空字符，表示如果取不到值，就返回一个空字符给account
    account = request.COOKIES.get('account', '')
    return render(request, 'test_view/login.html', {'account_two': account})


def index(request):
    person_list = models.person.objects.all()
    return render(request, 'test_view/index.html', {'person_list': person_list})


def add_person(request):
    if request.method == 'POST':
        # 取得姓名
        name = request.POST.get('name')
        # 取得邮箱
        email = request.POST.get('email')
        # 取得性别值
        gender = request.POST.get('gender')
        # 图片文件从request.FILES中取值
        head_img = request.FILES.get('head_img')
        # 文件类型从request.FILES中取值
        attachment = request.FILES.get('attachment')
        # 生成一条记录
        new_person = models.person.objects.create(name=name, email=email, gender=gender, head_img=head_img,
                                                  attachment=attachment)
        # 重定向
        return redirect('/test_view/index/')
    return render(request, 'test_view/add_person.html')


def edit_person(request, personid):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        head_img = request.FILES.get('head_img')
        attachment = request.FILES.get('attachment')
        person = models.person.objects.get(id=id)
        person.name = name
        person.emaul = email
        person.gender = gender
        # 判断前端网页传入值是否为空
        if head_img:
            # 头像文件有值时才修改数据字段的值
            person.head_img = head_img
        # 判断前端网页传入值是否为空
        if attachment:
            # 上传附件有值时才修改数据字段的值
            person.attachment = attachment
        person.save()
        return redirect('/test_view/index/')
    person_obj = models.person.objects.get(id=personid)
    return render(request,'test_view/edit_person.html',{'person':person_obj})
def del_person(request,personid):
    person_obj = models.person.objects.get(id=personid)
    person_obj.delete()
    return redirect('/test_view/index/')
