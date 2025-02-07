from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, 'todoapp/todo.html', {})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if len(password) < 3:
            messages.error(request, "Password must be at least 3 characters")
            return redirect('register')
        
        get_all_user_by_username = User.objects.filter(username=username)
        if get_all_user_by_username:
            messages.error(request, "Error, username already exists")
            return redirect('register')

        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()
        messages.success(request, 'User successfully created, login now!')
        return redirect('login')
    return render(request, 'todoapp/register.html', {})

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        validate_user = authenticate(username=username, password=password)
        if validate_user is not None:
            login(request, validate_user)
            return redirect('home-page')
        else:
            messages.error(request, 'Error, wrong user details or user does not exist')
            return redirect('login')
        

    print('request:', request)
    return render(request, 'todoapp/login.html', {})
