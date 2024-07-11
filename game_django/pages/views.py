from pdb import post_mortem
from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.urls import reverse, reverse_lazy
from django.views.generic import  *
from django.shortcuts import get_object_or_404, render
from pages.models import GameModel, GameModelForm

# Create your views here.


class GameListView(ListView):
    model = GameModel
    template_name = 'base.html'
    context_object_name = 'games'
    
    def get_queryset(self):
       super(GameListView, self).get_queryset()
       games = GameModel.objects.all().order_by('-pk')
       return games

class GameDetailView(DetailView):
    model = GameModel
    template_name = 'game_detail.html'
    context_object_name = 'game'



class GameCreateView(CreateView):  
      model = GameModel
      form_class = GameModelForm
      template_name = 'create.html'
      success_url = reverse('pages:list')


class GameDeleteView(DeleteView):
    model = GameModel  
    template_name = 'delete.html'
    success_url = reverse_lazy('pages:list')
    context_object_name = 'game'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(GameModel,pk=pk)
    
class GameUpdateView(UpdateView):
      model = GameModel
      form_class = GameModelForm
      template_name = 'update.html'
      success_url = reverse_lazy('pages:list')
      context_object_name = 'game'