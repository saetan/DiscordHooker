from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    authour = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    