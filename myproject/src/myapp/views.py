from django.shortcuts import render, HttpResponse
from .tasks import *

# Create your views here.
def home(request):
    show_hello_world.delay()
    return HttpResponse('Hello world!')