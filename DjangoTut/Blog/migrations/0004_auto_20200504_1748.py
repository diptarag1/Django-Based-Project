# Generated by Django 3.0.5 on 2020-05-04 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_remove_comment_title'),
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