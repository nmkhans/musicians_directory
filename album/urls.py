from django.urls import path
from . import views

urlpatterns = [
  path('add-album/', views.add_album, name = 'add-album'),
  path('edit-album/<int:id>', views.edit_album, name = 'edit-album'),
]
