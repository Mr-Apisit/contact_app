# Generated by Django 3.2.3 on 2021-05-26 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0005_alter_user_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
    ]
