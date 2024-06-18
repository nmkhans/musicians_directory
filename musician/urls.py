from django.urls import path
from . import views

urlpatterns = [
  path('add-musician/', views.add_musician, name = 'add-musician'),
  path('edit-musician/<int:id>', views.edit_musician, name = 'edit-musician')
]
