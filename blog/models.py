from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post (models.Model):
    user = models.ForeignKey (User, on_delete= models.CASCADE)
    content = models.TextField (blank= True)
    img = models.ImageField (upload_to= 'post_images/', blank= True , null='True')
    video = models.FileField (upload_to= 'post_videos/' , blank= True , null='True')
    timestamp = models.DateField (auto_now_add=True)

    def __str__(self):
        return f'Post by {self.user.username}'