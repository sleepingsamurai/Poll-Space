from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})

def register_view(request, *args, **kwargs):
    return render(request, 'register.html', {})  

def login_view(request, *args, **kwargs):
    return render(request, 'login.html', {})    