from django.shortcuts import render, redirect
from . forms import UserSignupform, UserLoginForm, AuthUserSignUpForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory, models
from django.contrib import messages
from django.views.decorators import gzip
from django.http import StreamingHttpResponse


def usersignup(request):
    form = UserSignupform()
    if request.method =='POST':
        form = UserSignupform(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created. ' + user)
            return redirect('userlogin')

    context = {'form':form}
    return render(request, 'users/1_register.html', context)


def loginpage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password incorrect')
    context = {}
    return render(request,'users/2_login.html', context)

def logoutusers(request):
    logout(request)
    return redirect('userlogin')



def authorsignup(request):
    author_form = AuthUserSignUpForm()
    if request.method =='POST':
        author_form = AuthUserSignUpForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            user = author_form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created. ' + user)
            return redirect('Authorsignup')

    context = {'author_form':author_form}
    return render(request, 'authors/1_author_register.html', context)

def authorlogin(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Authhome')
        else:
            messages.info(request, 'Username OR Password incorrect')

    context = {}
    return render(request, 'authors/2_author_login.html', context)

def authorlogout(request):
    logout(request)
    return redirect('Authorlogin')