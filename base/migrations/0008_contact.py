# Generated by Django 4.2.2 on 2023-06-22 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_gallery_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('subject', models.CharField(max_length=50, null=True)),
                ('message', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created', '-updated'],
            },
        ),
    ]
