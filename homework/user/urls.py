from django.urls import path
from user.views import login_site

urlpatterns = [
    path('',login_site)
]
