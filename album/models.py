from django.db import models
from musician.models import Musician

# Create your models here.

RATING_CHOICE = [
  ('1', '1'),
  ('2', '2'),
  ('3', '3'),
  ('4', '4'),
  ('5', '5'),
]

class Album(models.Model):
  name = models.CharField(max_length = 50)
  musician = models.OneToOneField(Musician, on_delete = models.CASCADE)
  release_date = models.DateField()
  rating = models.CharField(
    max_length = 50,
    choices = RATING_CHOICE,
    default = '1'
  )

  def __str__(self):
    return f'Album: {self.name}'