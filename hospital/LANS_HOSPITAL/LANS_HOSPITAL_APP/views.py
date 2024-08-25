from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return HttpResponse('Hello, world')

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request ,"about.html")

def test(request):
    return render(request ,"test.html")