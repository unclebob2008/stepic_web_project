from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 

def app(request, *args, **kwargs):
    return HttpResponse('OK')

def topnew(request, *args, **kwargs):
    return HttpResponse('TOPnew')

def toppop(request, *args, **kwargs):
    return HttpResponse('TOPpop')

def quone(request, *args, **kwargs):
    return HttpResponse('Quest 1')
