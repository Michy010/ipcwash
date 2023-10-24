from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Post (models.Model):
    user = models.ForeignKey (User, on_delete= models.CASCADE)
    content = models.TextField (blank= True)
    file = models.FileField (upload_to= 'post_files/' , blank= True , null=True)
    timestamp = models.DateField (auto_now_add=True)

    def __str__(self):
        return f'Post by {self.user.username}'
    

class Leader(models.Model):
    position = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='leader_images/', default='default.jpg', null=True, blank=True)

    # def save(self):
    #     super().save()
    #     img = Image.open (self.image.path) 

    #     if img.height > 1000 or img.width > 1000:
    #         output_size = (700, 700)
    #         img.thumbnail (output_size)
    #         img.save (self.image.path) 

    about_me = models.TextField()
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def _str_(self):
        return self.name
    
