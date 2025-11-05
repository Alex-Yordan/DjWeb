# test/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'test/home.html')

def page1(request):
    return render(request, 'test/page1.html')

def page2(request):
    return render(request, 'test/page2.html')

def page3(request):
    return render(request, 'test/page3.html')

def page4(request):
    return render(request, 'test/page4.html')