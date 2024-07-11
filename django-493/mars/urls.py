from django.urls import path
from .views import mars


urlpatterns = [
    path('mars/',mars),
]