# Generated by Django 3.2.7 on 2021-10-21 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_social_youtube_profile_social_github'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['name']},
        ),
    ]
