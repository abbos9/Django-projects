from django.shortcuts import render

# Create your views here.


def login_site(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
    return render(request, template_name='base.html')