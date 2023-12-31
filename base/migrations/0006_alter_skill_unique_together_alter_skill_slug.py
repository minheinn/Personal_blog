# Generated by Django 4.2.4 on 2023-09-01 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_gallery_slug'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='skill',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='skill',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=255, unique=True),
        ),
    ]
