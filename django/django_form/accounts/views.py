from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
#from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Create your views here.
def signup(request):

    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
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

def update(request):
    if reqeust.method=='POST':
        form = CustomUserChangeFor(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    } 

    return render(request, 'accounts/update.html', context)

def signin(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')


    form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signin.html', context)

@login_required
def signout(request):
    logout(request)
    return redirect('articles:index')

@require_POST
@login_required
def delete(request):
    request.user.delete()
    return redirect('articles:index')


def follow(request, pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=pk)
    
    if user != request.user:
        if user.followers.filter(pk=request.user.pk).exists():
            user.followers.remove(request.user)
        else:
            user.followers.add(request.user)
    
    return redirect('accounts:detail', user.pk)