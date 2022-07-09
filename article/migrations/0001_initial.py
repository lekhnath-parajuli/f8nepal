# Generated by Django 4.0.4 on 2022-07-07 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=100)),
                ('headline', models.CharField(max_length=150)),
                ('body', models.TextField()),
                ('author', models.CharField(max_length=30)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('cover_image', models.ImageField(upload_to='images/article/cover')),
                ('main_image', models.ImageField(upload_to='images/article/main')),
                ('author_profile', models.ImageField(upload_to='images/article/author')),
            ],
        ),
        migrations.CreateModel(
            name='Popular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Recommend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]