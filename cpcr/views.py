from pydoc import render_doc
from unicodedata import name
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import *
from .forms import CreateUserForm


@login_required(login_url='login')
def homepage(request):
    return render(request,'home.html')

@login_required(login_url='login')
def contactus(request):
    return render(request,'contact.html')

@login_required(login_url='login')
def profile(request):
    return render(request,'profile.html')

@login_required(login_url='login')
def signuppage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Accout created for ' + user)
            return redirect('login')

    context = {'form' : form}
    return render(request,'signup.html',context)


def loginpage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,'Username OR password is incorrect' )
    
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

