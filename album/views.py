from django.shortcuts import render, redirect
from .forms import AlbumForm
from .models import Album

# Create your views here.
def add_album(req):
  if req.method == 'POST':
    form = AlbumForm(req.POST)

    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    form = AlbumForm()

  return render(req, 'album/add_album.html', {'form': form})

def edit_album(req, id):
  album = Album.objects.get(pk = id)
  if req.method == 'POST':
    form = AlbumForm(req.POST, instance = album)

    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    form = AlbumForm(instance = album)

  return render(req, 'album/edit_album.html', {'form': form})