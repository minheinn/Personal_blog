# Generated by Django 4.2.2 on 2023-06-25 02:56

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_fact_fact_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='skill_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
