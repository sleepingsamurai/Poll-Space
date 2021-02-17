from django.shortcuts import render

# Create your views here.
def dashboard_view(request, *args, **kwargs):
    return render(request, 'polls/dashboard.html', {})

def vote_view(request, *args, **kwargs):
    return render(request, 'polls/vote.html', {})

def create_view(request, *args, **kwargs):
    return render(request, 'polls/create.html', {})