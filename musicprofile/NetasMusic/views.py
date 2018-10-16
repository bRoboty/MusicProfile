from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse(
       "<html><head><title>Index</title></head><body><h1>Hello Index page!</h1></body></html>")

