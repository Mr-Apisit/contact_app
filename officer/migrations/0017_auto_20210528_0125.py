# Generated by Django 3.2.3 on 2021-05-28 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0016_auto_20210527_0232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=15)),
                ('tag_slug', models.SlugField()),
            ],
        ),       
        migrations.AddField(
            model_name='member',
            name='skill_tag',
            field=models.ManyToManyField(to='officer.Tag'),
        ),
    ]
