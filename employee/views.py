# from django.shortcuts import render
# from django.template import loader
# # Create your views here.
# from django.http import HttpResponse

# def employee(request):
#     template=loader.get_template('edit.html')
#     return HttpResponse(template.render())

# def showemployee(request):
#     template=loader.get_template('show.html')
#     return HttpResponse(template.render())

# def registeremployee(request):
#     template=loader.get_template('index.html')
#     return HttpResponse(template.render())

from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm  
from employee.models import Employee  
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  

