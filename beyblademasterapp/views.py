from django.shortcuts import render
from django.views.generic.list import ListView
from beyblademasterapp.models import Beyblade
 
class HomePageView(ListView):
    model = Beyblade
    context_object_name = 'home'
    template_name = "base.html"
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        return context