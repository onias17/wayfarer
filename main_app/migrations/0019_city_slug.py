# Generated by Django 3.1.2 on 2020-11-04 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]