# Generated by Django 3.2.3 on 2021-05-26 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0010_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='officer.department'),
        ),
        migrations.AlterField(
            model_name='member',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='officer.position'),
        ),
        migrations.AlterField(
            model_name='member',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='officer.rank'),
        ),
    ]
