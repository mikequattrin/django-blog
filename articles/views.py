from django.shortcuts import render
from django.http import HttpResponse

# Article - App Views

def index(request):
    return HttpResponse("Hello, world. Here is the homepage.")

def articles(request):
    return HttpResponse("Hello, world. Here is a list of articles.")

def article(request):
    return HttpResponse("Hello, world. Here is an article.")
