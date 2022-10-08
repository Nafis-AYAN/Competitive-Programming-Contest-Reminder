from pydoc import render_doc
from django.shortcuts import render, HttpResponse

# Create your views here.

def homepage(request):
    return render(request,'home.html')

def contactus(request):
    return render(request,'contact.html')

def profile(request):
    return render(request,'profile.html')

def signup(request):
    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')

