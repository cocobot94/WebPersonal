from django.db import models


# Create your models here.
class Link(models.Model):
    title = models.CharField(max_length=200, default="Red Social")
    key = models.SlugField(max_length=100)
    url = models.URLField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Acerca(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="core", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Yo(models.Model):
    name = models.CharField(max_length=100, default="Elier Jerez")
    content = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="core")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Info(models.Model):
    country = models.IntegerField(default=1)
    telephone = models.IntegerField()
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
