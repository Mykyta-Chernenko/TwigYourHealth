# Generated by Django 2.0.5 on 2018-06-06 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0002_callentity_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatentity',
            name='hours',
            field=models.FloatField(blank=True, default=0, verbose_name='sum of hours spent on chat'),
        ),
    ]
