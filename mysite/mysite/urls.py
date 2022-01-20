"""mysite URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.contrib import admin
from django.urls import path
from django.views import View
import pathlib
import random
import os


def endeavour(req):
    new_var = HttpResponse("hello there!!")
    filename="fil.txt"+str(random.random())
    save_path = os.path.join(os.path.dirname(__file__),'all_files')
    completeName = os.path.join(save_path, filename)
    with open(filename, 'rb') as output:
        output.write(req.body)
    res={
        "success":True,
        "filename":filename
    }    
    return JsonResponse(res)

def download(req:HttpRequest, filename):
    save_path = os.path.join(os.path.dirname(__file__),'all_files')
    completeName = os.path.join(save_path, filename)
    with open(completeName,'rb') as m:
        content=m.read()
        return HttpResponse(content) 

def delte(req:HttpRequest, filename):
    file_del=pathlib.Path(filename)
    file_del.unlink()
    new_var = HttpResponse("file deleted")
    return new_var

def show(req):
    lst=[]
    path="C://Users//Deepika//Desktop//SPINNING WHEEL//mysite"
    for (root, dirs, file) in os.walk(path):
        for f in file:
            if '.txt' in f:
                lst.append(f)
                print(lst)
    return JsonResponse(lst,safe=False)

#class-based views
class file_view(View):
    def post(req):
            new_var = HttpResponse("hello there!!")
            filename="fil.txt"+str(random.random())
            with open(filename,'wb') as output:
                output.write(req.body)
            res={
                "success":True,
                "filename":filename
            }    
            return JsonResponse(res)
    def post(req:HttpRequest, filename):
        with open(filename,'rb') as m:
            content=m.read()
            return HttpResponse(content) 
    def get(req):
        lst=[]
        path="C://Users//Deepika//Desktop//SPINNING WHEEL//mysite"
        for (root, dirs, file) in os.walk(path):
            for f in file:
                if '.txt' in f:
                    lst.append(f)
                    print(lst)
        return JsonResponse(lst,safe=False)       

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ram', endeavour),
    path('data/<filename>', download),
    path('he/<filename>', delte),
    path('llll', show),
    path('a', file_view.as_view()),
    path('b/<filename>', file_view.as_view()),
    path('c', file_view.as_view()),
]
