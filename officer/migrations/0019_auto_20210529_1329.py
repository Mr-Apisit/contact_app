# Generated by Django 3.2.3 on 2021-05-29 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0018_remove_member_member_content'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.AddField(
            model_name='member',
            name='about_me',
            field=models.CharField(default='', max_length=200, null=True),
        ),
    ]
