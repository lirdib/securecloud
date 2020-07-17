from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    form = UserCreationForm()
    return  render(request,'authentication/signup.html', {'form':form})