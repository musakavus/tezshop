# Generated by Django 4.1.5 on 2023-05-21 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_registration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='subscription',
        ),
    ]