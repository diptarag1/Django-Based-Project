# Generated by Django 3.0.5 on 2020-05-05 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0008_auto_20200505_1742'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='dislikes',
            new_name='dislikers',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='likes',
            new_name='likers',
        ),
    ]
