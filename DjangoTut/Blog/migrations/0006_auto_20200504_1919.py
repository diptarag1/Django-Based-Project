# Generated by Django 3.0.5 on 2020-05-04 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_auto_20200504_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
