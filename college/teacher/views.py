from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# Create your views here.

def Class_Teacher(request):
    s='<h1> Abdul Kalam is Visiting faculty for our College </h1>'
    return HttpResponse(s)

def Subject(request):
    s='<h1> Abdul Kalam Teaches Aerodynamics in our college to students </h1>'
    return HttpResponse(s)
