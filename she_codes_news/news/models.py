from django.db import models
from django.contrib.auth import get_user_model


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(), 
        on_delete=models.CASCADE
        )
    pub_date = models.DateTimeField()
    content = models.TextField()
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.title

# COLOR_CHOICES = (
#     ('green'),
#     ('red')
# )
# class MyModel(models.Model):
#     color = models.CharField(max_length=6, choices = COLOR_CHOICES, default = 'green')