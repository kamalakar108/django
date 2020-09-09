from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Class(request):
    s='<h1> This first class in Django </h1>'
    return HttpResponse(s)

def Games(request):
    s='<h1> Students of this college like Playing Football </h1>'
    return HttpResponse(s)
