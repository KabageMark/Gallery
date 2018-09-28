from django.shortcuts import render,redirect
from .models import Image,Location,Category
# Create your views here.
def Gallery(request):
    image = Image.display_image()
    return render(request, 'index.html',{"image":image})


def news_today(request):
    date = dt.date.today()
    news = Article.today_news()
    return render(request,'all-news/today-news.html',{"date":date,"news":news})    