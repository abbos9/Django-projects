from django.shortcuts import render
from .models import News

# Create your views here.

def news_list(request):
    news = News.objects.all()
    context = {
        'news':news
    }
    return render(request, 'news.html', context=context)

def news_detail(request,pk):
    news = News.objects.get(pk=pk)
    context = {
        'news':news
    }
    return render(request, template_name='details.html',context=context)