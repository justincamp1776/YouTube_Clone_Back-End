# Generated by Django 3.2.8 on 2021-10-14 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20211014_0939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='commentId',
        ),
    ]