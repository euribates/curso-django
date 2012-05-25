#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

def perimetro_circunferencia(radio):
    import math
    perimetro = 2 * math.pi * radio
    return perimetro

radio = 6
print 'El perímetro de una circunferencia de radio'
print radio
print 'es'
print perimetro_circunferencia(radio)
