# Generated by Django 4.1.5 on 2023-12-09 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_post_create_slug_post_create_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_create',
            name='all_meta',
            field=models.TextField(blank=True, null=True),
        ),
    ]
