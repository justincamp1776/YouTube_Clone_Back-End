# Generated by Django 3.2.8 on 2021-10-14 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='videoId',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='reply',
            name='commentId',
            field=models.IntegerField(default=0),
        ),
    ]
