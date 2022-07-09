from django.contrib import admin
from article.models import (
    Article,
    Recommend,
    Popular
)

# Register your models here.
admin.register(Article) 
admin.register(Recommend) 
admin.register(Popular) 