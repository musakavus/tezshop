# Generated by Django 4.1.5 on 2023-05-21 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_registration_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='subscription',
            field=models.BooleanField(choices=[(True, 'Evet'), (False, 'Hayır')], default=False),
        ),
    ]