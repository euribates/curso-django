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

def homepage(request):
    t = Template('''<html>
    <head>
        <title>Shield.com homepage</title>
    </head>
    <body>
    <h1>Bienvenidos a S.H.I.E.L.D.</h1>
    <h2>Sistema Homologado de Inteligencia, Espionaje, Logística y Defensa</h2>
    <p>{{ message }}</p>
    </body>
    </html>''')
    ctx = RequestContext(request, {
        'message': '¡En obras! Pronto abriremos',
        })
    return HttpResponse(t.render(ctx))


def view_all_heroes(request):
    return render(request, 'not_imp.html', {
        'message': '¡En obras! Pronto abriremos',
        })
