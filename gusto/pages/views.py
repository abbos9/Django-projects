from django.shortcuts import render,redirect
from pages.forms import MessageForm 
from pages.models import MenuModel, SpecialsModel
# Create your views here.


def home_pages_view(request):
    desserts = MenuModel.objects.filter(category__title__icontains ='DESSERTS').order_by('-pk')
    dinner = MenuModel.objects.filter(category__title__icontains ='DINNER').order_by('-pk')
    main_course = MenuModel.objects.filter(category__title__icontains ='MAIN COURSE').order_by('-pk')
    breakfast = MenuModel.objects.filter(category__title__icontains ='BREAKFAST & STARTERS').order_by('-pk')
    special = SpecialsModel.objects.all()

    context = {
         'desserts': desserts,
         'dinners': dinner,
         'breakfasts': breakfast,
         'mains': main_course
    }

    return render(request, template_name='index.html', context=context)

def message_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
    else:
            return redirect('pages:home')
    return render(request, template_name='index.html')