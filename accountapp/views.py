from django.http import HttpResponse
from django.shortcuts import render

from accountapp.models import HelloWorld


# Create your views here.
def hello_world(requset):
    if requset.method == 'POST':

        temp = requset.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return render(requset, 'accountapp/hello_world.html', context={'hello_world_output': new_hello_world})
    else:
        return render(requset, 'accountapp/hello_world.html', context={'text': 'GET METHOD!!!'})
