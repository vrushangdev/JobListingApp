# Generated by Django 3.0.1 on 2019-12-30 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
    ]
