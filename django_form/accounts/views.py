from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, login, logout

from .forms import CustomUserChangeForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }

    return render(request, 'accounts/signup.html', context)

def detail(request, pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=pk)
    context = {
        'user': user,
    }

    return render(request, 'accounts/detail.html', context)

def update(request, pk):
    form = CustomUserChangeForm()
    context = {
        'form': form,
    } 

    return render(request, 'accounts/update.html', context)

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect('articles:index')


    form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signin.html', context)

def signout(request):
    logout(request)
    return redirect('articles:index')