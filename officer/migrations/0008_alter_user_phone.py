# Generated by Django 3.2.3 on 2021-05-26 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0007_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=10, null=True, verbose_name='phone'),
        ),
    ]
