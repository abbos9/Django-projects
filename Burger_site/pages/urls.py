from django.urls import path
from pages.views import (PageIndexView, PageAboutView,
PageContactView,PageElementView, PageMainView, PageMenuView,
LikedView,
)
app_name = 'pages'

urlpatterns = [
    path('', PageIndexView.as_view(), name ='home'),
    path('about/', PageAboutView.as_view(), name ='about'), 
    path('contact', PageContactView.as_view(), name ='contact'),
    path('elements/', PageElementView.as_view(), name ='elements'), 
    path('main/', PageMainView.as_view(), name='main'),
    path('menu/', PageMenuView.as_view(), name ='menu'), 
    path('liked/', LikedView.as_view(), name='liked'), 
]