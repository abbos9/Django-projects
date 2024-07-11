from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from authentifications.forms import SignUpForm
# Create your views here.

class SignupView(CreateView):
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('pages:signin')

    def form_valid(self, form):
        messages.success(self.request, "Account has been created for " + form.cleaned_data['username'])
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Account creation failed. Please correct the errors below.")
        return super().form_invalid(form)
    
def SigninView(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("pages:home")
    else:
        return render(request, 'signin.html',)

    

def Signout(request):
    logout(request)
    return render(request,template_name='index.html')