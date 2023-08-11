from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import User
from .forms import SignupForm, LoginForm, ForgotPasswordForm


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name  = form.cleaned_data['last_name']
            email      = form.cleaned_data['email']
            password   = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password == confirm_password:
                user = User(first_name=first_name, last_name=last_name, email=email, password=password, confirm_password=confirm_password)
                user.save()
                return HttpResponse("User created successfully")
            else:
                return HttpResponse("Password and Confirm Password does not match")
        else:
            return HttpResponse("Invalid Form")
    else:
        form = SignupForm()
        return render(request, 'user_login/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email    = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.filter(email=email, password=password).first()
            
            if user:
                request.session['user_id'] = user.id
                return render(request, 'user_login/home.html')
            else:
                return HttpResponse("Invalid Credentials")
        else:
            return HttpResponse("Invalid Form")
    else:
        form = LoginForm()
        return render(request, 'user_login/login.html', {'form': form})

def forgot_password(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email           = form.cleaned_data['email']
            new_password    = form.cleaned_data['new_password']
            confirm_password= form.cleaned_data['confirm_password']
            
            if new_password == confirm_password:
                user = User.objects.filter(email=email).first()
                if user:
                    user.password = new_password
                    user.confirm_password = confirm_password
                    user.save()
                    return HttpResponse("Password changed successfully")
                else:
                    return HttpResponse("User does not exist")
            else:
                return HttpResponse("Password and Confirm Password does not match")
        else:  
            return HttpResponse("Invalid Form")
    else:
        form = ForgotPasswordForm()
        return render(request, 'forgot_password.html', {'form': form})

@login_required(login_url='/login/')
def home(request):
    return render(request, 'user_login/signup.html')

def logout_user(request):
    logout(request)
    return redirect('/login/')

