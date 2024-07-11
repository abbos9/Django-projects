from django.shortcuts import render, redirect
from pages.forms import MessageForm, ReservationForm
from pages.models import AffordableModel, BaseModel
# Create your views here.
def home_view(request):
    all = AffordableModel.objects.all()
    category = AffordableModel.objects.all()
    bread = BaseModel.objects.filter(category__name__icontains="Bread")
    about = BaseModel.objects.filter(category__name__icontains="About Us")
    beer = BaseModel.objects.filter(category__name__icontains="Beer")
    dish = BaseModel.objects.filter(category__name__icontains="Dishes")

    context = {
        'all': all,
        'category': category,
        'breads':bread,
        'abouts':about,
        'beers':beer,
        'dishes':dish

    }
    return render(request, template_name='index.html',context=context)

def message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/')
        else:
            return render(request, template_name='index.html')
    else:
        return render(request, template_name='index.html')
    




def reservation_view(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pages:home')  
        else:
            return render(request, template_name='index.html',)
    else:
        form = ReservationForm()
        return render(request, template_name='index.html', )
