from pydoc import render_doc
from unicodedata import name
from django.shortcuts import render, HttpResponse

# Create your views here.

def homepage(request):
    dict = {
        'name': 'Nafis Sadique Ayan',
        'id' : 20101042,
        'email': '20101042@uap-bd.edu'
    }
    return render(request,'home.html',context=dict)

def contactus(request):
    return render(request,'contact.html')

def profile(request):
    return render(request,'profile.html')

def signup(request):
    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')

