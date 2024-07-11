from django.shortcuts import render

# Create your views here.
def mars(request):
    if request.method == "POST":
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        context = {
            "username": username,
            "phone": phone
        }
        return render(request, template_name="mars.html", context=context)
    return render(request, template_name="mars.html")