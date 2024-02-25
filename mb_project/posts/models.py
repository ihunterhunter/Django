from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]
