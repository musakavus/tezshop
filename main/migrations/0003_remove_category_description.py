# Generated by Django 4.1.5 on 2023-05-21 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
    ]
