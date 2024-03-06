import traceback

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

from employee.models import employee, department, group, employee_info


# 部门表操作
# list_dep_old.html页面内容
def list_dep_old(request):
    dep_list = department.objects.all()
    # 取出数据表全部记录
    # render()函数有三个参数，第一个参数request是固定的；第二个参数是HTML文件；
    # 第三个参数是字典类型，这个参数值传给HTML文件，在网页中以模版变量形式放置在相应的位置。
    return render(request, 'test_orm_old/list_dep_old.html', {'dep_list': dep_list})


# 添加部门数据表数据
def add_dep_old(request):
    # 判断请求方式，如为POST说明前端页面要提交数据
    if request.method == 'POST':
        dep_name = request.POST.get('dep_name')
        dep_script = request.POST.get('dep_script')
        if dep_name.strip() == '':
            return render(request, 'test_orm_old/add_dep_old.html', {'error_info': '部门名称不能为空！'})
        try:
            # 用create()函数新建一条记录，这条记录会自动保存，不用调用save()函数
            department.objects.create(dep_name=dep_name, dep_script=dep_script)
            # obj = department(dep_name=dep_name, dep_script=dep_script)
            # obj.save()
            # dic = {"dep_name": dep_name, "dep_script": dep_script}
            # department.objects.create(dic)
            # redirect()重定向，参数是一个字符串，匹配的是URL配置项；
            # 即执行views.py中list_dep_old()视图函数，这个函数由URL配置项中path()函数第二个参数指定
            return redirect('/test_orm_old/list_dep_old/')
        except Exception as e:
            traceback.print_exc()
            return render(request, 'test_orm_old/add_dep_old.html', {'error_info': '输入部门名称重复或信息有错误！'})
        finally:
            pass
    return render(request, 'test_orm_old/add_dep_old.html')


# 删除部门数据表数据
def del_dep_old(request, dep_id):
    # 通过get()函数取得一条记录
    dep_object = department.objects.get(id=dep_id)
    dep_object.delete()
    return redirect('/test_orm_old/list_dep_old')


# 修改部门数据表数据
def edit_dep_old(request, dep_id):
    # 判断请求方式
    if request.method == 'POST':
        id = request.POST.get('id')
        # 获取前端页面提交的数据
        dep_name = request.POST.get('dep_name')
        dep_script = request.POST.get('dep_script')
        dep_object = department.objects.get(id=dep_id)
        # 给字段赋值
        dep_object.dep_name = dep_name
        dep_object.dep_script = dep_script
        # 保存数据到数据库表
        dep_object.save()
        return redirect('/test_orm_old/list_dep_old/')
    else:
        dep_object = department.objects.get(id=dep_id)
        return render(request, 'test_orm_old/edit_dep_old.html', {'department': dep_object})


# 团体表操作
def list_group_old(request):
    group_list = group.objects.all()
    return render(request, 'test_orm_old/list_group_old.html', {'group_list': group_list})


def add_group_old(request):
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        group_script = request.POST.get('group_script')
        # 当团体名称为空时，向网页传递错误信息
        if group_name.strip() == '':
            return render(request, 'test_orm_old/add_group_old.html', {'error_info': '团体名称不能为空！'})
        try:
            group.objects.create(group_name=group_name, group_script=group_script)
            return redirect('/test_orm_old/list_group_old/')
        except Exception as e:
            # traceback.print_exc()
            return render(request, 'test_orm_old/add_group_old.html', {'error_info': '输入团体名称重复或信息有错误！'})
        finally:
            pass
    return render(request, 'test_orm_old/add_group_old.html')


def del_group_old(request, group_id):
    group_object = group.objects.get(id=group_id)
    group_object.delete()
    return redirect('/test_orm_old/list_group_old')


def edit_group_old(request, group_id):
    if request.method == 'POST':
        id = request.POST.get('id')
        group_name = request.POST.get('group_name')
        group_script = request.POST.get('group_script')
        group_object = group.objects.get(id=id)
        group_object.group_name = group_name
        group_object.group_script = group_script
        group_object.save()
        return redirect('/test_orm_old/list_group_old/')
    else:
        group_object = group.objects.get(id=group_id)
        return render(request, 'test_orm_old/edit_group_old.html', {'group': group_object})


# 员工补充信息表操作
def list_employeeinfo_old(request):
    empinfo_list = employee_info.objects.all()
    return render(request, 'test_orm_old/list_empinfo_old.html', {'empinfo_list': empinfo_list})


def add_employeeinfo_old(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        if phone.strip() == '':
            return render(request, 'test_orm_old/add_empinfo_old.html', {'error_info': '电话号码不能为空！'})
        try:
            employee_info.objects.create(phone=phone, address=address)
            return redirect('/test_orm_old/list_empinfo_old/')
        except Exception as e:
            return render(request, 'test_orm_old/add_empinfo_old.html', {'error_info': '信息有错误！'})
        finally:
            pass
    return render(request, 'test_orm_old/add_empinfo_old.html')


def del_employeeinfo_old(request, info_id):
    empinfo_object = employee_info.objects.get(id=info_id)
    empinfo_object.delete()
    return redirect('/test_orm_old/list_empinfo_old')


def edit_employeeinfo_old(request, info_id):
    if request.method == 'POST':
        id = request.POST.get('id')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        empinfo_object = employee_info.objects.get(id=info_id)
        empinfo_object.phone = phone
        empinfo_object.address = address
        empinfo_object.save()
        return redirect('/test_orm_old/list_empinfo_old/')
    else:
        empinfo_object = employee_info.objects.get(id=info_id)
        return render(request, 'test_orm_old/edit_empinfo_old.html', {'empinfo': empinfo_object})


# 员工表操作
def list_employee_old(request):
    emp_list = employee.objects.all()
    return render(request, 'test_orm_old/list_emp_old.html', {'emp_list': emp_list})


def add_employee_old(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        dep = request.POST.get('dep')
        info = request.POST.get('info')
        salary = request.POST.get('salary')
        # 取多个值
        groups = request.POST.getlist('group')
        new_emp = employee.objects.create(name=name, email=email, salary=salary, dep_id=dep, info_id=info)
        new_emp.group.set(groups)
        return redirect('/test_orm_old/list_emp_old/')
    dep_list = department.objects.all()
    group_list = group.objects.all()
    info_list = employee_info.objects.all()
    return render(request, 'test_orm_old/add_emp_old.html',
                  {'dep_list': dep_list, 'group_list': group_list, 'info_list': info_list})


def del_employee_old(request, emp_id):
    emp_object = employee.objects.get(id=emp_id)
    emp_object.delete()
    return redirect('/test_orm_old/list_emp_old')


def edit_employee_old(request, emp_id):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        salary = request.POST.get('salary')
        dep = request.POST.get('dep')
        info = request.POST.get('info')
        groups = request.POST.getlist('group')
        emp = employee.objects.get(id=emp_id)
        emp.name = name
        emp.email = email
        emp.salary = salary
        emp.dep_id = dep
        emp.info_id = info
        emp.group.set(groups)
        emp.save()
        return redirect('/test_orm_old/list_emp_old/')
    emp = employee.objects.get(id=emp_id)
    dep_list = department.objects.all()
    group_list = group.objects.all()
    info_list = employee_info.objects.all()
    return render(request, 'test_orm_old/edit_emp_old.html',
                  {'emp': emp, 'dep_list': dep_list, 'group_list': group_list, 'info_list': info_list})
