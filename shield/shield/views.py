#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response

from shield import models

import datetime

def homepage(request):
    return render_to_response(
        'shield/homepage.html',
        locals())

def heroes(request):
	heroes = models.Heroe.objects.all()
	return render_to_response(
        'shield/heroes.html',
        locals())