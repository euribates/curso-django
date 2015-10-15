#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from django.http import HttpResponse
from django.template import Template, RequestContext
from django.shortcuts import render
from metahumans import models

# Create your views here.




def all_heroes(request):
    return render(request, 'metahumans/list_heroes.html', {
        'heroes': models.SuperHero.objects.select_related('team').all(),
        'title': 'Listado de superhéroes',
        })

def list_levels(request):
    return render(request, 'metahumans/levels.html', {
        'heroes': models.SuperHero.objects.only('name', 'level').all().order_by('-level'),
        'title': 'Listado de superhéroes por niveles',
        })

def detail_hero(request, slug):
    sh = models.SuperHero.objects.get(slug=slug)
    return render(request, 'metahumans/details_hero.html', {
        'superhero': sh,
        'title': sh.name,
        })

