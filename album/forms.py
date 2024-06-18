from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
  class Meta:
    model = Album
    fields = '__all__'

    widgets = {
      'name': forms.TextInput(attrs = {'placeholder': 'Enter album name...'}),
      'release_date': forms.NumberInput(attrs = {'type': 'date'})
    }