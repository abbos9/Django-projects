from django.urls import path

from games.views import GamesListView, GamesDetailView, GamesCreateView, GameDeleteView, \
    GamesUpdateView

app_name = 'games'

urlpatterns = [
    path('', GamesListView.as_view(), name='list'),
    path('<int:pk>', GamesDetailView.as_view(), name='detail'),
    path('create/', GamesCreateView.as_view(), name='create'),
    path('<int:pk>/delete/', GameDeleteView.as_view(), name='delete'),
    path('<int:pk>/update/', GamesUpdateView.as_view(), name='update')
]