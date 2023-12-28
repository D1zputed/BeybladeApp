from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from beyblademasterapp.models import *
from beyblademasterapp.forms import *
from django.urls import reverse_lazy
 
class HomePageView(ListView):
    model = Beyblade
    context_object_name = 'home'
    template_name = "base.html"
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        return context
    
class PlayerListView(ListView):
    model = Player
    context_object_name = 'players'
    template_name = 'players.html'
    paginate_by = 5

class PlayerCreateView(CreateView):
    model = Player
    form_class = PlayerForm
    template_name = 'player_add.html'
    success_url = reverse_lazy('player-list')

class PlayerUpdateView(UpdateView):
    model = Player
    form_class = PlayerForm
    template_name = 'player_edit.html'
    success_url = reverse_lazy('player-list')
    
class PlayererDeleteView(DeleteView):
    model = Player
    template_name = 'player_del.html'
    success_url = reverse_lazy('player-list')