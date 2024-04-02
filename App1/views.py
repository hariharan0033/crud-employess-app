from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def employee(request):
    emp=Employee.objects.all()
    return render(request,'Employee.html',{'employees':emp})

def insert_employee(request):
    form = EmployeeForm()       #blankform 
    if request.method=='POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listemp')
        
    return render(request,'employee_form.html',{'form':form,'action':"Add"})

def delete_employee(request,i):
    if request.method == 'POST':    
        emp=Employee.objects.get(id=i)
        emp.delete()
        return redirect('listemp')
    return render(request,'delete.html')

def update_employee(request,i):
    emp = Employee.objects.get(id=i)
    form = EmployeeForm(instance=emp)       #blankform 
    if request.method=='POST':
        form = EmployeeForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return redirect('listemp')
    return render(request,'employee_form.html',{'form':form,'action':"Update"})

def registerPage(request):
    form = UserCreationForm
    if  request.method=="POST":
        form =UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listemp')
    return render(request,'register.html',{"form":form})