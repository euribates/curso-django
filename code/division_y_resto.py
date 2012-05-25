#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

def division_y_resto(dividendo, divisor):
    return dividendo // divisor, dividendo % divisor

cociente, resto = division_y_resto(47, 9)
print 'cociente:', cociente
print 'resto:', resto
