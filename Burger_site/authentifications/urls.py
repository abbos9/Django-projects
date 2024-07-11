from django.urls import path

from authentifications.views import Signout, SigninView, SignupView

app_name = 'auth'

urlpatterns = [
    path('signout/', Signout, name='signout'),
    path('signin/', SigninView, name='signin'),
    path("signup/", SignupView.as_view(), name='signup'),
]