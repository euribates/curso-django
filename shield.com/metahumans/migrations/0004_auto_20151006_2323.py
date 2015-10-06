# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('metahumans', '0003_auto_20151006_2251'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='power',
            options={'verbose_name': 'Poder', 'verbose_name_plural': 'Poderes'},
        ),
        migrations.AddField(
            model_name='superhero',
            name='alter_ego',
            field=models.CharField(max_length=120, blank=True),
        ),
        migrations.AlterField(
            model_name='capabilities',
            name='scale',
            field=models.PositiveIntegerField(default=10, validators=[django.core.validators.MaxValueValidator(10)]),
        ),
    ]
