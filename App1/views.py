from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def employee(request):
    emp=Employee.objects.all()
    return render(request,'Employee.html',{'employees':emp})
@login_required(login_url='login')
def insert_employee(request):
    form = EmployeeForm()       #blankform 
    if request.method=='POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listemp')
        
    return render(request,'employee_form.html',{'form':form,'action':"Add"})
@login_required(login_url='login')
def delete_employee(request,i):
    if request.method == 'POST':    
        emp=Employee.objects.get(id=i)
        emp.delete()
        return redirect('listemp')
    return render(request,'delete.html')
@login_required(login_url='login')
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

def loginPage(request):
    if request.method=='POST':
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        user=authenticate(request,username=uname,password=pwd)
        if user is None:
            print("Invalid username / password")
        else:
            login(request,user)
            return redirect('listemp')
    return render(request,'login.html')

def logoutPage(request):
    logout(request)
    return redirect('login')