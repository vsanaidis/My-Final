# Generated by Django 5.0.6 on 2024-07-19 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0013_note_post_like_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='post',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='note',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.DeleteModel(
            name='Note',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
