# Generated by Django 3.0.5 on 2020-05-04 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_auto_20200504_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='points',
        ),
        migrations.RemoveField(
            model_name='post',
            name='points',
        ),
    ]
