from django.shortcuts import render,HttpResponse
from.models import Employee

# Create your views here.
def display(request,emp_id):
    emp = Employee.objects.filter(Emp_Id = emp_id)
    context = {"emp":emp}
    return render(request ,"index.html",context)

from django.shortcuts import render,redirect,HttpResponse
from app2.models import Employee
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        
        if password != cpassword:
            messages.error(request, "Passwords do not match")
            return redirect('/signin')
        
        try:
            user = User.objects.get(username=username)
            messages.error(request, "Username already taken")
            return redirect('/signin')
        except User.DoesNotExist:
            pass
        
        try:
            user = User.objects.get(email=email)
            messages.error(request, "Email already taken")
            return redirect('/signin')
        except User.DoesNotExist:
            pass
        
        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        messages.success(request, "User created successfully. Please log in.")
        return redirect('/login')
    
    return render(request, "signin.html")

def handlelogin(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password = request.POST.get('password')
        myuser=authenticate(request,username=username,password=password)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,'Login Successfully')
            return HttpResponse("LOGIN Succesfull")
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('/login')
            
        
    return render(request,"login.html")