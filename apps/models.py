from django.db import models

# Create your models here.

class Notifica (models.Model):

    email = models.EmailField()