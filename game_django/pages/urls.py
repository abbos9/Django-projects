from django.urls import path
# from pages.views import 
from pages.views import GameListView, GameDetailView, GameCreateView, GameDeleteView, UpdateView

app_name = 'pages'

urlpatterns = [
    path('', GameListView.as_view(), name='list'),
    path('<int:pk>',GameDetailView.as_view() ,name='detail'),
    path('<int:pk>/create/',GameCreateView.as_view() ,name='create'),
    path('<int:pk>/delete/',GameDeleteView.as_view() ,name='delete'),
    path('<int:pk>/update/',UpdateView.as_view() ,name='update'),
]
