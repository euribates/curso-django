#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from django.core.exceptions import ValidationError

def between_zero_and_one_hundred(value):
    if value < 0 or value > 100:
        raise ValidationError('El nivel de poder debe oscilar entre 0 y 100.')

