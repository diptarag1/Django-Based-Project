# Generated by Django 3.0.5 on 2020-05-05 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200504_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='disliked_posts',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='liked_posts',
        ),
    ]
