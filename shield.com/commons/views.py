#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.



def homepage(request):
    return render(request, 'homepage.html', {
        'title': 'Página de inicio',
        'message': '¡En obras! Pronto abriremos',
        })
