from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "home.html")

def hello(request):
    return HttpResponse("Hello MIT Class")


def emobilis(request):
    return HttpResponse("This is emobilis")


def new(request):
    return render(request, "new.html")