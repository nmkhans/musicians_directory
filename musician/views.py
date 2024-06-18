from django.shortcuts import render, redirect
from .forms import MusicianForm
from .models import Musician

# Create your views here.
def add_musician(req):
  if req.method == 'POST':
    form = MusicianForm(req.POST)
    
    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    form = MusicianForm()

  return render(req, 'musician/add_musician.html', {'form': form})

def edit_musician(req, id):
  musician = Musician.objects.get(pk = id)

  if req.method == 'POST':
    form = MusicianForm(req.POST, instance = musician)

    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    form = MusicianForm(instance = musician)

  return render(req, 'musician/edit_musician.html', {'form': form})