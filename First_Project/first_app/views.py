from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    diction = {}
    return render(request,'first_app/index.html',context=diction)

def test(request):
    return HttpResponse("<h1>This is a test page</h1>")

def home(request):
    return HttpResponse("<h1>This is home page</h1> <a href='contact/'>Contact</a> <a href='about/'>About</a>")

def contact(request):
    return HttpResponse("<h1>This is contact page</h1> <a href='/'>HomePage</a> <a href='/about/'>About</a>")

def about(request):
    return HttpResponse("<h1>About us</h1> <a href='/'>HomePage</a> <a href='/contact/'>Contact</a>")