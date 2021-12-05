from django.db import models

# Create your models here.

class travelus(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='imgs')
    disc = models.TextField()

    def __str__(self):
        return self.name

class travelteem(models.Model):
    name = models.CharField(max_length=250)
    Image = models.ImageField(upload_to='pic')
    disc = models.TextField()

    def __str__(self):
        return self.name