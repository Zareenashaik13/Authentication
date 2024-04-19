
from django.shortcuts import render,redirect
from app2.models import Employee

# Create your views here.
def details(request):
    if request.method == "POST":
        name=request.POST.get('name')
        emp_id=request.POST.get('emp_id')
        designation=request.POST.get('designation')
        location=request.POST.get('location')
        employee,created =Employee.objects.get_or_create(Name =name ,Emp_Id = emp_id,Designation = designation,Location=location)
        return render(request,"details.html",{})
    else:
        return render(request,"details.html",{})
