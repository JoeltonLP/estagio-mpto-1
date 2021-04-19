from django.db import models
from django.db.models.fields import CharField


class State(models.Model):
    name = models.CharField('Nome', max_length=100, unique=True)
    abbreviation = models.CharField('Sigla', max_length=2, unique=True)