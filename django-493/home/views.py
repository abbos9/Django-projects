from django.shortcuts import render
from django.http import HttpResponse
from .models import News
# Create your views here.


def index(request):
    result = 0
    if request.method == "POST":
        num_1 = int(request.POST.get("num_1"))
        op = request.POST.get("op")
        num_2 = int(request.POST.get("num_2"))
        if op == "+":
            result = num_1 + num_2
        elif op == "-":
            result = num_1 - num_2
        elif op == "*":
            result = num_1 * num_2
        elif op == "/":
            result = num_1 // num_2
        
    context = {
            "result": result
        }
    return render(request, template_name="index.html", context=context)


def registration(request):
    if request.method == "POST":
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        context = {
            "username": username,
            "phone": phone
        }
        return render(request, template_name="forms.html", context=context)
    return render(request, template_name="forms.html")

def news_list(request):
    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, template_name='news.html', context=context)

def news_detail(request,pk):
    news = News.objects.get(pk=pk)
    context = {
        'news': news
    }
    return render(request, template_name='news_detail.html', context=context)
