from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def signin(request):
    form = UserCreationForm()
    return  render(request,'authentication/signup.html', {'form':form})