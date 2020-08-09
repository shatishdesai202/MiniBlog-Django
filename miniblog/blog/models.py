from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    post_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    message = models.TextField()
    email = models.EmailField()