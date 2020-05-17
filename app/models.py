from django.contrib.auth.models import User
from django.db import models

class News(models.Model):
    action = models.CharField(max_length=200)
    text = models.TextField(max_length=2000)
    data = models.DateField(auto_now=True)

    def __str__(self):
        return "Новости"

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
        ordering = ['-data']