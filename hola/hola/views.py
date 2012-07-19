#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse

def hola(request):
    return HttpResponse("Hola, mundo")
