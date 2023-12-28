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
    paginate_by = 3

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
    
class PlayerDeleteView(DeleteView):
    model = Player
    template_name = 'player_del.html'
    success_url = reverse_lazy('player-list')
    
class MentorListView(ListView):
    model = Mentor
    context_object_name = 'mentors'
    template_name = 'mentors.html'
    paginate_by = 3

class MentorCreateView(CreateView):
    model = Mentor
    form_class = MentorForm
    template_name = 'mentor_add.html'
    success_url = reverse_lazy('mentor-list')

class MentorUpdateView(UpdateView):
    model = Mentor
    form_class = MentorForm
    template_name = 'mentor_edit.html'
    success_url = reverse_lazy('mentor-list')
    
class MentorDeleteView(DeleteView):
    model = Mentor
    template_name = 'mentor_del.html'
    success_url = reverse_lazy('mentor-list')
    
class AddressListView(ListView):
    model = CurAddress
    context_object_name = 'addresses'
    template_name = 'address.html'
    paginate_by = 3

class AddressCreateView(CreateView):
    model = CurAddress
    form_class = AddressForm
    template_name = 'address_add.html'
    success_url = reverse_lazy('address-list')

class AddressUpdateView(UpdateView):
    model = CurAddress
    form_class = AddressForm
    template_name = 'address_edit.html'
    success_url = reverse_lazy('address-list')
    
class AddressDeleteView(DeleteView):
    model = CurAddress
    template_name = 'address_del.html'
    success_url = reverse_lazy('address-list')
    
class CollectionListView(ListView):
    model = Collection
    context_object_name = 'collections'
    template_name = 'collections.html'
    paginate_by = 5
    
class CollectionCreateView(CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collection_add.html'
    success_url = reverse_lazy('collection-list')
    
class CollectionUpdateView(UpdateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collection_edit.html'
    success_url = reverse_lazy('collection-list')
    
class CollectionDeleteView(DeleteView):
    model = Collection
    template_name = 'collection_del.html'
    success_url = reverse_lazy('collection-list')