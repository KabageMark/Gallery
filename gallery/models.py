from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    def save_location(self):
        return self.save()        

class Category(models.Model):
    name = models.CharField(max_length=60,blank=True)

    def __str__(self):
        return self.name

    def save_category(self):
        return self.save()    
 

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

    def get_image_by_id(cls,incoming_id):
        image_result = cls.objects.get(id=incoming_id)
        return image_result    
   
    def save_image(self):
        return self.save()
        
    def delete_image(self):
        return self.delete() 

    @classmethod
    def retrieve_all(cls):
        all_objects = Image.objects.all()
        for item in all_objects:
            return item;    

    @classmethod
    def search_by_category(cls,search_term):
        image = Image.objects.filter(category__name__icontains=search_term)
        return image
        
    @classmethod
    def display_by_location(cls,location):
        image = Image.objects.filter(location__name__icontains=location)
        return image

    @classmethod
    def update_image(cls,current_value,new_value):
        fetched_object = Image.objects.filter(name=current_value).update(name=new_value)
        return fetched_object
        

