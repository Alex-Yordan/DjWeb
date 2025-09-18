from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1> Главная страница проекта на Джанго </h1>")

def test(request):
    return HttpResponse("<h1> Страница Test </h1>")

def data(request):
    return HttpResponse("<h1> Страница Data </h1>")