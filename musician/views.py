from django.shortcuts import render

# Create your views here.
def add_musician(req):
  return render(req, 'musician/add_musician.html')