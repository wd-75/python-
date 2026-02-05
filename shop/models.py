from django.db import models

# Create your models here.
# Create your DB table here.

# null = False for sql ,,, blank = False for html 
class Student(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)
    age = models.IntegerField()
    email = models.EmailField(null=True, blank=True)  
    faculty = models.CharField(max_length=255,null=False, blank=False, default='BCA')
    collage = models.CharField(max_length=255,null=False, blank=False, default='MMAMC')
    verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    short_description = models.CharField(max_length=500)
    stock = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    verified = models.BooleanField(default=False)    
    
    def __str__(self):
        return self.title