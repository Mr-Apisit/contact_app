# Generated by Django 3.2.3 on 2021-05-29 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0017_auto_20210528_0125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='member_content',
        ),
    ]