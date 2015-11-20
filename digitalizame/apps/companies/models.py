from django.db import models

# Create your models here.

class Type(models.Model):
    description = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='media/icons', blank=None, null=True)

class Companies(models.Model):
    type = models.ForeignKey(Type)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=None, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    tags = models.TextField()
    slug = models.SlugField(blank=None, null=True)
    is_activate = models.DateTimeField(blank=None, null=True)
    picture = models.ImageField(upload_to='media/companies', blank=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
