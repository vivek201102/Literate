from platform import platform
from django.db import models

# Create your models here.

class help(models.Model):
    command = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class funchat(models.Model):
    question1 = models.CharField(max_length=255)
    question2 = models.CharField(max_length=255)
    question3 = models.CharField(max_length=255)
    question4 = models.CharField(max_length=255)
    question5 = models.CharField(max_length=255)
    answer1 = models.CharField(max_length=255)
    answer2 = models.CharField(max_length=255)
    answer3 = models.CharField(max_length=255)

class courses(models.Model):
    url = models.CharField(max_length=255)
    course_name = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    instructor = models.CharField(max_length=255)
    price = models.IntegerField()
    tag1 = models.CharField(max_length=255)
    tag2 = models.CharField(max_length=255)
    tag3 = models.CharField(max_length=255)
    
