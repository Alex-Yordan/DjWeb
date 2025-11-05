from django.shortcuts import render
from .models import NewPost

# Create your views here.
def home(request):
    news = NewPost.objects.all()
    return render(request, 'news/news.html', {'news': news })