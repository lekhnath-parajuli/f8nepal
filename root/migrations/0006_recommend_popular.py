# Generated by Django 4.0.4 on 2022-07-09 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0005_delete_popular_delete_recommend'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField(max_length=512)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='root.article')),
            ],
        ),
        migrations.CreateModel(
            name='Popular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField(max_length=512)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='root.article')),
            ],
        ),
    ]
