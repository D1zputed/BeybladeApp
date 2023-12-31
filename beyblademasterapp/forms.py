from django.forms import ModelForm
from django import forms
from .models import Player, Collection, Beyblade, Mentor, CurAddress
class PlayerForm(ModelForm):
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Player
        fields = "__all__"
        
class BeybladeForm(ModelForm):
    release_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Beyblade
        fields = "__all__"
        
class CollectionForm(ModelForm):
    acquisition_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Collection
        fields = "__all__"
        
class MentorForm(ModelForm):
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Mentor
        fields = "__all__"
        
class AddressForm(ModelForm):
    class Meta:
        model = CurAddress
        fields = "__all__"