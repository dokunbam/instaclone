from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Photo(models.Model):
    post = models.TextField(max_length=140, default="")
    image_file = models.ImageField(upload_to='public/images', default='image.png')
    image_url = models.CharField(max_length=140, default='image.png')
    date_uploaded = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    tags = models.IntegerField(default=0)

    class Meta:
        ordering = ('date_uploaded',)

    def __str__(self):
        return self.post