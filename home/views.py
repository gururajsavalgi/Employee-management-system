from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

# Create your views here.

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'all_employee.html', context)


def add_emp(request):
    
    print("outside")
    if request.method=='POST':
        print("inside")
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        salary = request.POST.get('salary')
        bonus = request.POST.get('bonus')
        phone = request.POST.get('phone')
        dept = request.POST.get('dept')
        role = request.POST.get('role')
        new_emp = Employee(first_name= first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept_id = dept, role_id = role, hire_date = datetime.now())
        new_emp.save()
        return HttpResponse('Employee added Successfully')
    elif request.method=='GET':
        role=Role.objects.all()
        dept=Department.objects.all()
        params={'role':role,'dept':dept}
        return render(request, 'add_emp.html',params)
    else:
        return HttpResponse("An Exception Occured! Employee Has Not Been Added")
    

def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html',context)


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)

        context = {
            'emps': emps
        }
        return render(request, 'view.html', context)

    elif request.method == 'GET':
        return render(request, 'filter.html')
    else:
        return HttpResponse('An Exception Occurred')
    

def load_subcategories(request, dept_id):
    print("Inside load_subcategories view function")
    try:
        roles = Role.objects.filter(dept_id=dept_id).order_by('name')
        roles_list = [{'id': role.id, 'name': role.name} for role in roles]
        return JsonResponse(roles_list, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)