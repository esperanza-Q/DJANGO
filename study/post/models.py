from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Image(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    image=models.ImageField(upload_to = 'images/', null=True, blank =True)
    
