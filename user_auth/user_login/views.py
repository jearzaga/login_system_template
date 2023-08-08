from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'user_login/index.html')

def signup(request):
    return HttpResponse("Hello, world. You're at Signup page.")

def login(request):
    return HttpResponse("Hello, world. You're at Login page.")
