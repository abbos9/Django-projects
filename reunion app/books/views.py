
from books.models import Book, Genre, Currency
from django.shortcuts import render, redirect
from books.forms import homework
from django.db.models import Q
import requests

# Create your views here.

def get_weather(request):
    url = requests.get('https://api.openweathermap.org/data/2.5/weather?q=tashkent&appid=e1408599974bfafd4add9fe2282cd73e').json()
    context = {
        'weather': url
    }
    # text = ''
    # for person in data:
    #     text += person['name'] + '\n'
    
    return render(request=request,template_name='weather.html', context=context)

def book_list(request):
    q = request.GET.get('q')
    genres = Genre.objects.all()
    genre = request.GET.get("genre")
    if q:
        try:
            books = Book.objects.filter(
                Q(title__icontains=q) |
                Q(author__first_name__icontains=q) |
                Q(author__last_name__icontains=q) |
                Q(price__gte=q)
            )
        except Exception:
            books = Book.objects.filter(
                Q(title__icontains=q) |
                Q(author__first_name__icontains=q) |
                Q(author__last_name__icontains=q)
            )
    elif genre:
        books = Book.objects.filter(genre__title=genre)
    else:
        books = Book.objects.all()
    context = {
        "books": books,
        'genres': genres
    }
    return render(request, template_name='books.html', context=context)


def genre_icon_viwer(request, pk):
    genre_icon = Genre.GET.get('genre')
    if genre_icon:
        genres = Book.objects.filter(
            Q(title__icontains=genre_icon)
        )
    else:
        genres = Genre.objects.all()
    context = {
        'genre': genres
    }
    return render(request=request, template_name='books.html', context=context)


def book_details(request,pk):
    book_detail =  Book.objects.get(pk=pk)
    context = {
        "detail_book": book_detail
    }
    return render(request,template_name='detail.html',context=context)

def book_delate(request,pk):
    book =  Book.objects.get(pk=pk)
    book.delete()
    return redirect('http://127.0.0.1:8000/books/list/')



def form_data(request):
    form = homework()
    if request.method == 'POST':
        form = homework(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/books/list/')
    context = {'form': form}
    return render(request, template_name='add.html',context=context)


def update_book(request,pk):
    book =  Book.objects.get(id=pk)
    form = homework(instance=book)
    if request.method == "POST":
         form = homework(request.POST,request.FILES)
         if form.is_valid():
             form.save()
             return redirect("http://127.0.0.1:8000/books/list/")
         
    return render(request,"update.html",{'form':form})


def get_currency(request):
    url = requests.get('https://nbu.uz/exchange-rates/json/')
    data = url.json()
    currency_codes = []
    buy  =[]
    sell = []
    title = []
    result = 0 
     
    total = Currency.objects.all()
    
    for currency in data:
        title.append(currency['title'])
        buy.append(currency['nbu_cell_price'])
        sell.append(currency['nbu_buy_price'])


    Currency.objects.create(title = title, nbu_buy_price=buy, nbu_cell_price = sell)

    if request.method == "POST":
       code = request.POST.get('code')
       ammount = request.POST.get('ammount')
       for currency in data:
           if currency['code'] == code:
               result = float(ammount) * float(currency['cb_price']) 
               
    context = {
        'codes': currency_codes,
        'result': f"{result}.",
        'titles': title,
        'buys': buy,
        'sells': sell,
        'all': total
    }
    return render(request=request,template_name='currency.html', context=context)