#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator
from django.utils.encoding import python_2_unicode_compatible

from .validators import between_zero_and_one_hundred

# Create your models here.

@python_2_unicode_compatible
class Power(models.Model):

    class Meta:
        db_table = 'mh_power'
        verbose_name = 'Poder'
        verbose_name_plural = 'Poderes'

    name = models.CharField(max_length=32, unique=True)
    slug = models.SlugField(max_length=32, unique=True)
    description = models.CharField(max_length=530, blank=True)

    def __str__(self):
        return self.description

@python_2_unicode_compatible
class Team(models.Model):
    
    class Meta:
        db_table = 'mh_team'
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'

    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=60, unique=True)
    created = models.DateField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    headquarters = models.CharField(max_length=500, blank=True)
    description = models.CharField(max_length=530, blank=True)

    def __str__(self):
        if self.active:
            return self.name
        else:
            return '{} (Inactivo)'.format(self.name)



@python_2_unicode_compatible
class SuperHero(models.Model):

    class Meta:
        db_table = 'mh_superhero'
        verbose_name = 'Superhéroe'
        verbose_name_plural = 'Superhéroes'

    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=60, unique=True)
    level = models.IntegerField(
        default=0,
        validators=[between_zero_and_one_hundred,]
        )
    created = models.DateField('Fecha de creación', auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    email = models.EmailField(blank=True)
    team = models.ForeignKey(Team, blank=True, null=True)
    powers = models.ManyToManyField(Power, through='Capabilities')
    description = models.CharField(max_length=530, blank=True)
    alter_ego = models.CharField(max_length=120, blank=True)

    def __str__(self):
        if self.team:
            return '{} ({})'.format(self.name, self.team.name)
        else:
            return self.name

    def list_of_powers(self):
        powers = list(self.powers.all())
        if powers:
            return ', '.join([_.name for _ in powers])
        else:
            return 'Ninguno.'

@python_2_unicode_compatible
class Capabilities(models.Model):

    class Meta:
        db_table = 'mh_capabilities'
        verbose_name = 'Capacidad'
        verbose_name_plural = 'Capacidades'

    superhero = models.ForeignKey('SuperHero')
    power = models.ForeignKey('Power')
    scale = models.PositiveIntegerField(
        default=10,
        validators=[MaxValueValidator(10)]
        )

    def __str__(self):
        return '{} puede {} ({} escala {})'.format(
            self.superhero.name,
            self.power.description,
            self.power.name,
            self.scale,
            )
