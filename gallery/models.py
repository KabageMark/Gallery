from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=60)


class Category(models.Model):
    name = models.CharField(max_length=60) 

class Image(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to = 'gallery/')
    descripition = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ManyToManyField(Category)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    @classmethod
    def display_image(cls):
        images = cls.objects.all()
        return images

    def search_by_category(cls,search_term):
        image = cls.objects.filter(category__icontains=search_term)
        return image
    
        

