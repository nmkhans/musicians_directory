from django.urls import path
from . import views

urlpatterns = [
  path('add-album/', views.add_album, name = 'add-album'),
  path('edit-album/<int:id>', views.edit_album, name = 'edit-album'),
  path('delete-album/<int:id>', views.delete_album, name = 'delete-album'),
]
