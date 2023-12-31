# Generated by Django 4.2.2 on 2023-06-26 07:43

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_skill_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True),
        ),
    ]
