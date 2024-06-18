from django.shortcuts import render
from album.models import Album

def home(req):
  albums = Album.objects.all()

  return render(req, 'index.html', {'albums': albums})