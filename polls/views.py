from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Polls, Voted

# Create your views here.
def dashboard_view(request, *args, **kwargs) :
    polls = Polls.objects.all()
    context = {
        'polls' : polls
    }
    return render(request, 'polls/dashboard.html', context)

def vote_view(request, poll_id, *args, **kwargs) :
    poll = Polls.objects.get(pk = poll_id)
    context = {
        'poll' : poll
    }
    return render(request, 'polls/vote.html', context)

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

def login_view(request) :
    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None :
            login(request, user)
            messages.success(request, 'heyyy')
            return redirect('dashboard')
    return render(request, 'polls/login.html', {})
