from django.db import models
from user.models import user

# Create your models here.
class book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    price = models.IntegerField()
    status = models.CharField(max_length=50)
    image = models.ImageField(upload_to = "books")
    user = models.ForeignKey(user, on_delete= models.CASCADE)
