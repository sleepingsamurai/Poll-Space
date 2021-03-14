from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages

# Create your views here.
def dashboard_view(request, *args, **kwargs) :
    return render(request, 'polls/dashboard.html', {})

def vote_view(request, *args, **kwargs) :
    return render(request, 'polls/vote.html', {})

def create_view(request, *args, **kwargs) :
    return render(request, 'polls/create.html', {})

def result_view(request, *args, **kwargs) :
    return render(request, 'polls/result.html', {})

def register_view(request) :
    form = CreateUserForm()

    if request.method == 'POST' :
        form = CreateUserForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('login')

    context = {'form': form}
    return render(request, 'polls/register.html', context)

def login_view(request, *args, **kwargs) :
    return render(request, 'polls/login.html', {})