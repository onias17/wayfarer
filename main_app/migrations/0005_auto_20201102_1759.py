# Generated by Django 3.1.2 on 2020-11-02 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='media/images/default-profile-img.png', upload_to='images/'),
        ),
    ]
