# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
import metahumans.validators


class Migration(migrations.Migration):

    dependencies = [
        ('metahumans', '0002_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capabilities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scale', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10)])),
                ('power', models.ForeignKey(to='metahumans.Power')),
            ],
            options={
                'db_table': 'mh_capabilities',
                'verbose_name': 'Capacidad',
                'verbose_name_plural': 'Capacidades',
            },
        ),
        migrations.CreateModel(
            name='SuperHero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=60)),
                ('slug', models.SlugField(unique=True, max_length=60)),
                ('level', models.IntegerField(default=0, validators=[metahumans.validators.between_zero_and_one_hundred])),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('description', models.CharField(max_length=530, blank=True)),
                ('powers', models.ManyToManyField(to='metahumans.Power', through='metahumans.Capabilities')),
                ('team', models.ForeignKey(blank=True, to='metahumans.Team', null=True)),
            ],
            options={
                'db_table': 'mh_superhero',
                'verbose_name': 'Superh\xe9roe',
                'verbose_name_plural': 'Superh\xe9roes',
            },
        ),
        migrations.AddField(
            model_name='capabilities',
            name='superhero',
            field=models.ForeignKey(to='metahumans.SuperHero'),
        ),
    ]
