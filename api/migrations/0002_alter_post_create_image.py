# Generated by Django 4.1.5 on 2023-12-09 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_create',
            name='image',
            field=models.FileField(default='', upload_to='autopost/'),
        ),
    ]
