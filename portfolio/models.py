from django.db import models
from ckeditor.fields import RichTextField
from hitcount.models import HitCountMixin,HitCount
from django.contrib.contenttypes.fields import GenericRelation


class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return f"{self.full_name} {self.email}"


class Chocolate(models.Model):
    image = models.ImageField(upload_to='Images/chocolate')
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
class About(models.Model):
    image = models.ImageField(upload_to='Images/about')
    title = models.CharField(max_length=70)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    


   
class Testimonial(models.Model):
    image = models.ImageField(upload_to='Images/testimonial')
    title = models.CharField(max_length=70)
    description = models.TextField()
    
    def __str__(self):
        return self.title