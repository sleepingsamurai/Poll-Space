from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Polls

class CreateUserForm(UserCreationForm) :
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

class CreatePollForm(ModelForm) :
    class Meta:
        model = Polls
        fields = [
            'poll_question',
            'poll_option1',
            'poll_option2',
            'poll_option3',
            'poll_option4'
        ]       