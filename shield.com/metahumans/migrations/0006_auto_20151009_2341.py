# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metahumans', '0005_superhero_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superhero',
            name='created',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de creaci\xf3n'),
        ),
    ]
