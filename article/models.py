from django.db import models

class Article(models.Model):
    head = models.CharField(max_length=100)
    headline = models.CharField(max_length=150)
    body = models.TextField()
    author = models.CharField(max_length=30)
    posted_on = models.DateTimeField(auto_now_add = True)
    cover_image = models.ImageField(upload_to='images/article/cover')
    main_image = models.ImageField(upload_to='images/article/main')
    author_profile = models.ImageField(upload_to='images/article/author')
 
class Recommend(models.Model):
    pass

class Popular(models.Model):
    pass