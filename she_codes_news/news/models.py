from unicodedata import category
from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE
        )
    pub_date = models.DateTimeField()
    content = models.TextField()
    image = models.CharField(max_length=1000)
    category = models.CharField(max_length=200, default='Cakes')

    def __str__(self):
        return self.title

