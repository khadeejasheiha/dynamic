from django.db import models


# Create your models here.
class pclass(models.Model):
    head = models.CharField(max_length=300)
    des = models.CharField(max_length=3009)
    img = models.ImageField(upload_to='pic')


class data(models.Model):
    heading = models.CharField(max_length=255)
    desig = models.CharField(max_length=1235)
    imgs = models.ImageField(upload_to='pic')


class con(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mess = models.CharField(max_length=1000)


class abc(models.Model):
    names = models.CharField(max_length=23)
    designations = models.CharField(max_length=2345)
    images = models.ImageField(upload_to='pic')
