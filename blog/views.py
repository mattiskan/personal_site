from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello world")


def create(request):
    return HttpResponse("This will create a new blog entry in the future!")
