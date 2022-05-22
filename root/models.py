from pyexpat import model
from xml.etree.ElementTree import Comment
from django.db import models

# Create your models here.

class Feedback(models.Model):
    Catagory = models.CharField(max_length=30)
    Rating = models.IntegerField()
    FullName = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    Comment = models.CharField(max_length=200)


class Team(models.Model):
    profile = models.ImageField(upload_to='images/team')
    FullName = models.CharField(max_length=30)
    Position = models.CharField(max_length=30)
    Twitter  = models.CharField(max_length=200)
    Facebook = models.CharField(max_length=200)
    Instagram = models.CharField(max_length=200)
    LinkedIn  = models.CharField(max_length=200)

class Services(models.Model):
    image = models.ImageField(upload_to='images/services')
    ServiceName = models.CharField(max_length=30)
    Discription = models.CharField(max_length=500)
    RedirectLink = models.CharField(max_length=500)
    Fade = models.CharField(max_length=30)
    Delay = models.CharField(max_length=30)


class Portfolio(models.Model):
    image = models.ImageField(upload_to='images/portfolio')
    ProjectName = models.CharField(max_length=30)
    ToolUsed = models.CharField(max_length=200)
    Link = models.CharField(max_length=200)

class Customers(models.Model):
    image = models.ImageField(upload_to='images/clients')
    Name = models.CharField(max_length=30)
    PositionAndCompanyName = models.CharField(max_length=30)
    Discription = models.CharField(max_length=200)
    Fade = models.CharField(max_length=30)
    Delay = models.CharField(max_length=30) 
