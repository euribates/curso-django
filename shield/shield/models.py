#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

class Equipo(models.Model):
    nombre_equipo = models.CharField(max_length=60)
    f_creacion = models.DateField()
    Direccion = models.TextField()
 
    def __unicode__(self):
        return self.nombre_equipo
    
class Poder(models.Model):
    nombre_poder = models.CharField(max_length=32)
    descripcion = models.CharField(max_length=500)

    def __unicode__(self):
        return u'%s (%s)' % (self.nombre_poder, self.descripcion)

GRUPO_SANGUINEO = (
    ('O', 'O (Universal)'),
    ('A', 'Grupo A'),
    ('B', 'Grupo B'),
    ('AB', 'Grupo AB'),
    )

class Heroe(models.Model):
    nombre_heroe = models.CharField(max_length=120)
    identidad = models.CharField(max_length=170)
    f_nacimiento = models.DateField()
    nivel = models.IntegerField()
    grupo_sanguineo = models.CharField(
        max_length=2, 
        choices=GRUPO_SANGUINEO,
        )
    foto = models.FileField(upload_to='fotos')
    correo = models.EmailField(blank=True)
    equipo = models.ForeignKey(Equipo, blank=True, null=True)
    poderes = models.ManyToManyField(Poder)

    def __unicode__(self):
        return self.nombre_heroe

class Avistamiento(models.Model):
    f_avistamiento = models.DateTimeField()
    latitud = models.FloatField()
    longitud = models.FloatField()
    heroe = models.ForeignKey(Heroe)

    def __unicode__(self):
        return '%s en %.6f, %.2f, el %s' % (
            self.heroe,
            self.latitud,
            self.longitud,
            self.f_avistamiento
            )