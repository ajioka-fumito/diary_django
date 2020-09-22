from django.db import models
from django.utils import timezone

class Day(models.Model):
    title = models.CharField('title',max_length=200)
    text = models.TextField('text')
    date = models.DateField('date',default=timezone.now)

class Comment(models.Model):
    comment_id = models.ForeignKey(to=Day,on_delete=models.CASCADE)
    comment = models.TextField('comment')
    date = models.DateTimeField('date',auto_now_add=True)