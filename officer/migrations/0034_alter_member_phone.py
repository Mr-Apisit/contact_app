# Generated by Django 3.2.3 on 2021-05-31 13:59

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0033_alter_member_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]