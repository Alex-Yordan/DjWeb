from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1> Мой первый проект на Джанго </h1>")

def new(request):
    return HttpResponse("<h1> Вторая страница проекта на Джанго </h1>")