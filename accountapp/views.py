from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def hello_world(requset):
    return render(requset, 'accountapp/hello_world.html')
