# Generated by Django 3.2.3 on 2021-05-31 04:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0028_alter_tag_tag_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 31, 4, 26, 24, 277310)),
        ),
    ]
