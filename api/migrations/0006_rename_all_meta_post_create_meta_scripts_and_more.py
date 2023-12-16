# Generated by Django 4.1.5 on 2023-12-09 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_post_create_all_meta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post_create',
            old_name='all_meta',
            new_name='meta_scripts',
        ),
        migrations.AddField(
            model_name='post_create',
            name='meta_tags',
            field=models.TextField(blank=True, null=True),
        ),
    ]