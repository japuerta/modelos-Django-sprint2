from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("prueba aplicacion")