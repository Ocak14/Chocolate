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



# class About(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     image = models.ImageField(upload_to='Images/about')
    
#     def __str__(self):
#         return self.title
    
