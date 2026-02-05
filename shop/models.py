from django.db import models

# Create your models here.
# Create your DB table here.

# null = False for sql ,,, blank = False for html 
class Student(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)
    age = models.IntegerField()
    email = models.EmailField(null=True, blank=True)    

