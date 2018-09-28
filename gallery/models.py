from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=60)


class Category(models.Model):
    name = models.CharField(max_length=60) 

class Image(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to = 'articles/')
    descripition = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ManyToManyField(Category)
    pub_date = models.DateTimeField(auto_now_add=True)

