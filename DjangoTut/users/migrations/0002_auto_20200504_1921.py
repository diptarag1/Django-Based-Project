# Generated by Django 3.0.5 on 2020-05-04 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_auto_20200504_1919'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='disliked_posts',
            field=models.ManyToManyField(related_name='dislikedposts', to='Blog.Post'),
        ),
        migrations.AddField(
            model_name='profile',
            name='liked_posts',
            field=models.ManyToManyField(related_name='likedposts', to='Blog.Post'),
        ),
    ]