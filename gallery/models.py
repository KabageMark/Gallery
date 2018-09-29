from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=60,blank=True)

    def __str__(self):
        return self.name
 

class Image(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to = 'gallery/')
    descripition = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    @classmethod
    def display_image(cls,category):
        images = cls.objects.filter(category__name=category)
        return images

    def display_id(cls):
        images = cls.objects.all()
        return images    

    def search_by_category(cls,search_term):
        image = cls.objects.filter(category__icontains=search_term)
        return image
    
        

