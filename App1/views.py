from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm
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
        
    return render(request,'insert_employee.html',{'form':form})