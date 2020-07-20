from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('index')
    else:
        form = UserCreationForm()
    return  render(request,'authentication/signup.html', {'form':form})


def account(request):
    username = request.user
    data = {'username': username}
    return render(request, 'authentication/account.html', data)