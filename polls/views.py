from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,CreatePollForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Polls, Voted

# Create your views here.
def dashboard_view(request, *args, **kwargs) :
    polls = Polls.objects.all()
    votedpolls = request.user.voted_set.all()
    active = []
    for poll in polls :
        if Voted.objects.filter(user=request.user,poll=poll) :
           continue
        else :
           active.append(poll)
    context = {
        'polls' : polls,
        'votedpolls' : votedpolls,
        'active' : active
    }
    return render(request, 'polls/dashboard.html', context)

def vote_view(request, poll_id, *args, **kwargs) :
    poll = Polls.objects.get(pk = poll_id)

    if request.method == 'POST' :
        selected = request.POST['one']
        if selected == 'poll_option1' :
            poll.poll_option1_count += 1
        elif selected == 'poll_option2' :
            poll.poll_option2_count += 1
        elif selected == 'poll_option3' :
            poll.poll_option3_count += 1
        elif selected == 'poll_option4' :
            poll.poll_option4_count += 1
        poll.save()
        Voted.objects.create(user = request.user, poll = poll)
        return redirect('result',poll_id)
    context = {
        'poll' : poll
    }
    return render(request, 'polls/vote.html', context)

def create_view(request, *args, **kwargs) :
    if request.method == 'POST' :
        form = CreatePollForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('dashboard')
    else :    
        form = CreatePollForm()
    context = {
        'form' : form
    }
    return render(request, 'polls/create.html', context)
 
def result_view(request, poll_id, *args, **kwargs) :
    poll = Polls.objects.get(pk = poll_id)
    context = {
        'poll' : poll
    }
    return render(request, 'polls/result.html', context)

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
