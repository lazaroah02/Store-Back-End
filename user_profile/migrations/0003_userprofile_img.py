# Generated by Django 4.0.4 on 2022-09-10 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_alter_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures'),
        ),
    ]
