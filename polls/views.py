from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    message = "Hello, world."
    return HttpResponse(message)