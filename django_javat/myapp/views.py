from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from myapp.forms import EmployeeForm

def emp(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                return redirect('/')  
            except:  
                pass  
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  

def hello(request):
    return HttpResponse("<h2>Hello, Welcome to Django!</h2>")