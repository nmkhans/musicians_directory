from django.shortcuts import render, redirect
from .forms import AlbumForm

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