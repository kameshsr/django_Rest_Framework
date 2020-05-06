from django.db import models

# Create your models here.

class Article(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.IntegerField()
    image = models.ImageField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

