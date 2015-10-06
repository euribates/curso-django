# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Power',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32)),
                ('slug', models.SlugField(unique=True, max_length=32)),
                ('description', models.CharField(max_length=530, blank=True)),
            ],
            options={
                'db_table': 'mh_power',
                'verbose_name': 'Superpoder',
                'verbose_name_plural': 'Superpoderes',
            },
        ),
    ]
