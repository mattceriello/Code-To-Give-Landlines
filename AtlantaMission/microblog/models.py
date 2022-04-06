from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

## timezone.now provides current time based on our timezone
## django by default have a User model

# Create your models here.

## User to Post - One to Many Relationship

## Redirect will redirect you to a specific route
## Reverse will return your full url to the route as a string

class Post(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=50)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('individual_post', kwargs={'pk': self.pk})