# Generated by Django 4.0.4 on 2022-07-08 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0002_article_popular_recommend'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pdf',
            field=models.FileField(default=None, upload_to='images/article/pdfs'),
        ),
    ]
