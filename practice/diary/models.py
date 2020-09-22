from django.db import models
from django.utils import timezone

class Day(models.Model):
    title = models.CharField('title',max_length=200)
    text = models.TextField('text')
    date = models.DateField('date',default=timezone.now)