# Generated by Django 3.2.3 on 2021-05-29 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0020_auto_20210529_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
