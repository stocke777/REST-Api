from django.db import models

# Create your models here.

class Article(models.Model):   # Model for Article

    title = models.CharField(max_length=100)   
    author = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)   # date is automatically added when article created

    def __str__(self):   # return the title when an object of this model is called in print(), repr(), etc
        return self.title