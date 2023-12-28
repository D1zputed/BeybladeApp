from django.forms import ModelForm
from django import forms
from .models import Player, Collection, Beyblade, Mentor, CurAddress
class PlayerForm(ModelForm):
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Player
        fields = "__all__"
        
class BaybladeForm(ModelForm):
    release_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Beyblade
        fields = "__all__"
        
class CollectionForm(ModelForm):
    collection_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Collection
        fields = "__all__"