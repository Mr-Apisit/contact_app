# Generated by Django 3.2.3 on 2021-05-26 10:41

from django.db import migrations, models
# import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0013_auto_20210526_0941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='article_content',
        ),
        migrations.RemoveField(
            model_name='member',
            name='article_slug',
        ),
        migrations.AlterField(
            model_name='article',
            name='article_content',
            field=models.TextField(),
            # field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_slug',
            field=models.SlugField(),
        ),
    ]
