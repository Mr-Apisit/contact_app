# Generated by Django 3.2.3 on 2021-05-31 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0036_alter_member_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(max_length=13, unique=True),
        ),
    ]