#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext

def homepage(request):
    ctx = { 'message': '¡En obras! Pronto abriremos' }
    return render(request, 'homepage.html', context=ctx)
