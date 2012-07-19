#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from shield.models import Heroe, Poder
from shield.models import Equipo, Avistamiento

admin.site.register(Heroe)
admin.site.register(Poder)
admin.site.register(Equipo)
admin.site.register(Avistamiento)

