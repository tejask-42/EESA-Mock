from django.db import models

class SlideImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()

class LogoImages(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()

class CouncilPhotos(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    link = models.URLField(max_length=200)
    image = models.ImageField()
