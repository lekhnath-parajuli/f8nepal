from django.urls import path

from .views import (
    article_home_view
)

urlpatterns = [
    path('', article_home_view, name="article-home")
]
