from django.db import models


class Card(models.Model):
    deck = models.ForeignKey('Deck', on_delete=models.CASCADE)
    front = models.TextField()
    back = models.TextField()

class Deck(models.Model):
    title = models.CharField(max_length=60)

# Create your models here.
