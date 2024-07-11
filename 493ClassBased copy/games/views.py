from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from games.forms import GamesModelForm
from games.models import GamesModel


# def games_list_view(request):
#     games = GamesModel.objects.all()
#     context = {
#         'games': games
#     }
#     return render(request, 'games.html', context)


class GamesListView(ListView):
    model = GamesModel
    template_name = 'games.html'
    context_object_name = 'games'


# def game_detail_view(request, pk):
#     game = get_object_or_404(GamesModel, pk=pk)
#     context = {'game': game}
#     return render(request, 'game_detail.html', context)

class GamesDetailView(DetailView):
    model = GamesModel
    template_name = 'game_detail.html'
    context_object_name = 'game'


# def game_create_view(request):
#     if request.method == 'POST':
#         form = GamesModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('games:list')
#     else:
#         form = GamesModelForm()
#         context = {'form': form}
#         return render(request, 'game_create.html', context)


class GamesCreateView(CreateView):
    model = GamesModel
    form_class = GamesModelForm
    template_name = 'game_create.html'
    success_url = reverse_lazy('games:list')


# def game_delete_view(request, pk):
#     game = get_object_or_404(GamesModel, id=pk)
#     if request.method == 'POST':
#         game.delete()
#         return redirect('games:list')
#     return render(request, 'delete_confirm.html', {'game': game})

class GameDeleteView(DeleteView):
    model = GamesModel
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('games:list')
    context_object_name = 'game'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(GamesModel, pk=pk)


# def game_update_view(request, pk):
#     game = get_object_or_404(GamesModel, pk=pk)
#     if request.method == 'POST':
#         form = GamesModelForm(request.POST, instance=game)
#         if form.is_valid():
#             form.save()
#             return redirect('games:list')
#     else:
#         form = GamesModelForm(instance=game)
#         context = {'form': form, 'game': game}
#         return render(request, 'game_update.html', context)


class GamesUpdateView(UpdateView):
    model = GamesModel
    form_class = GamesModelForm
    template_name = 'game_update.html'
    success_url = reverse_lazy('games:list')
    context_object_name = 'game'
